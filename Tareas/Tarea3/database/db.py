import pymysql as psql
import uuid as uu
import os, json
from utils.clases import Donation,Order


#* function that put the donation in DB
def searchCommune(name_commune):
    def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    
    with open('database/comunas-chile.json') as json_file:
        data = json.load(json_file)
        
    inComunne = next((obj for obj in data if normalize(obj["name"]) == name_commune), None)

    
    if inComunne:
        lng = inComunne["lng"]
        lat = inComunne["lat"]
        return lng, lat
    else:
        return None

def conection(userConnection):
	conn = psql.connect(
		db="tarea2",
		user=userConnection["USER"],
		passwd=userConnection["PASSWORD"],
		host=userConnection["HOST"],
		port=3306,
		charset="utf8"
	)
	return conn

def getInfoGrafic(userConnection):
    mySQL = conection(userConnection)
    mycursos = mySQL.cursor()
    
    sol = f"SELECT tipo FROM donacion"
    mycursos.execute(sol)
    dataDonation = mycursos.fetchall()
    
    sol = f"SELECT tipo FROM pedido"
    mycursos.execute(sol)
    dataOrder = mycursos.fetchall()
    
    donations = {}
    for i in dataDonation:
        _tipe = i[0]

        if _tipe not in donations:
            donations[_tipe] = 1
        else:
            donations[_tipe] = 1 + donations[_tipe]
        
            
    order = {}
    for i in dataOrder:
        _tipe = i[0]
        if _tipe not in order:
            order[_tipe] = 1
        else:
            order[_tipe] = 1 + order[_tipe]
        
    return donations, order

def getInfoMap(userConnection):
    mySQL = conection(userConnection)
    mycursos = mySQL.cursor()
    sol = f"SELECT comuna_id, id, calle_numero, tipo, cantidad, fecha_disponibilidad, email FROM donacion ORDER BY id DESC LIMIT 5"
    mycursos.execute(sol)
    dataDonation = mycursos.fetchall()
    sol = f"SELECT comuna_id, id, tipo, cantidad, email_solicitante FROM pedido ORDER BY id DESC LIMIT 5"
    mycursos.execute(sol)
    dataOrder = mycursos.fetchall()

    
    donations = []
    orders = []
    
    infCommune = []
    communesInData = []
    for i in dataDonation:
        _data = {
            'id' : i[1],
            'calle': i[2],
            'tipo': i[3],
            'cantidad'  : i[4],
            'fecha-disponible' : i[5]
        }
        _nameCommune = getCommuneID(userConnection, i[0])[0][2]
        if _nameCommune in communesInData:
            ubq = communesInData.index(_nameCommune)
            lng, lat = infCommune[communesInData.index(_nameCommune)]
            donations[ubq][1].append(_data)
        else:
            communesInData.append(_nameCommune)
            tr = searchCommune(_nameCommune)
            if tr:
                lng, lat = tr
            else:
                return "error"
            infCommune.append( (lng, lat) )
            donations.append([{'lng' : lng, 'lat': lat}, [_data]])
            
    
    infCommune = []
    communesInData = []
    for i in dataOrder:
        _data = {
            'id': i[1],
            'tipo': i[2],
            'cantidad': i[3],
            'email': i[4]
        }
        _nameCommune = getCommuneID(userConnection, i[0])[0][2]
        if _nameCommune in communesInData:
            ubq = communesInData.index(_nameCommune)
            lng, lat = infCommune[communesInData.index(_nameCommune)]
            orders[ubq][1].append(_data)
        else:
            communesInData.append(_nameCommune)
            tr = searchCommune(_nameCommune)
            if tr:
                lng, lat = tr
            else:
                return "error"
            infCommune.append( (lng, lat) )
            orders.append([{'lng' : lng, 'lat': lat}, [_data]])
        
        
    
    return donations, orders

def getRegion(userConnection):
    mySQL = conection(userConnection)
    mycursos = mySQL.cursor()
    mycursos.execute(f"SELECT id, nombre FROM region")
    data = mycursos.fetchall()
    mycursos.close()
    return data

def getRegionID(userConnection,id):
    mySQL = conection(userConnection)
    mycursos = mySQL.cursor()
    mycursos.execute(f"SELECT id, nombre FROM region WHERE id = {id}")
    data = mycursos.fetchone()
    mycursos.close()
    return data

def getCommune(userConnection, region:int = None):
    mySQL = conection(userConnection)
    mycursor = mySQL.cursor()
    if region == None:
        mycursor.execute(f"SELECT region_id ,id , nombre FROM comuna")
    else:
        mycursor.execute(f"SELECT region_id ,id , nombre FROM comuna WHERE region_id = {str(region)}")
    data = mycursor.fetchall()
    mycursor.close()
    return data

def getCommuneID(userConnection, id:int):
    mySQL = conection(userConnection)
    mycursor = mySQL.cursor()
    mycursor.execute(f"SELECT region_id ,id , nombre FROM comuna WHERE id = {str(id)}")
    data = mycursor.fetchall()
    mycursor.close()
    return data

def saveDonate(donation:Donation,userConnection):
    #!We will to considerate the donation is valid
    mySQL = conection(userConnection)
    myCursor = mySQL.cursor()
    myCursor.execute(f"INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES ('{donation.commune_id}',' {donation.address}', '{donation.typeD}','{donation.amount_donation}','{donation.date_available}', '{donation.description}', '{donation.condition}','{donation.name}', '{donation.email}', '{donation.phone_number}')")
    myId = myCursor.lastrowid
    mySQL.commit()
    return myId

def savePhotos(id_donation:int, request, userConnection,UPLOAD_FILE = "static/uploads"):
    mySQL = conection(userConnection)
    mycursos = mySQL.cursor()
    photos = request.files.getlist('fotos')
    for photo in photos:
        _fileName = str(uu.uuid4()) + os.path.splitext(photo.filename)[1].lower() 
        photo.seek(0)
        _ContentBytes = photo.read()
        routeNewFile = os.path.join(UPLOAD_FILE,_fileName)
        with open(routeNewFile, "wb") as archive:
            archive.write(_ContentBytes)
        
        mycursos.execute(f"INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES ('{UPLOAD_FILE}','{_fileName}','{id_donation}')")
        mySQL.commit()
    mySQL.close()

def getPhotos(userConnection,idUser):
    mySQL = conection(userConnection)
    mycursor = mySQL.cursor()
    sentence = f"SELECT ruta_archivo, nombre_archivo FROM foto WHERE donacion_id = {idUser}"
    mycursor.execute(sentence)
    _photos = mycursor.fetchall()
    mySQL.close()
    return _photos

def saveOrder(order:Order,userConnection):
    mySQL = conection(userConnection)
    mycursos = mySQL.cursor()
    sentence = f"INSERT INTO pedido (comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES ("
    save = f'"{order.commune}","{order.type_order}","{order.description}","{order.amount}","{order.name}","{order.email}","{order.number_phone}"'
    mycursos.execute(sentence+save+")")
    mySQL.commit()
    mySQL.close()
    
def getDonation(userConnection, pag = 1):
    mySQL = conection(userConnection)
    mycursor = mySQL.cursor()
    sentence = f"SELECT * FROM donacion LIMIT {(pag-1)*5},5"
    mycursor.execute(sentence)
    donations = mycursor.fetchall()
    mySQL.close()
    return donations
    
    
def get5Donation(userConnection,pag = 1):
    _donations = getDonation(userConnection, pag)
    donations = []
    for _donation in _donations:
        _photos = getPhotos(userConnection,_donation[0])
        photosForDonation = []
        for i in _photos:
            photosForDonation.append(f"uploads/{i[1]}")
        

        donation = {
            "commune": getCommuneID(userConnection, _donation[1])[0][2],
            "type": _donation[3],
            "ammount": _donation[4],
            "date": _donation[5],
            "name": _donation[8],
            "dir":"static",
            "photo":photosForDonation,
            "id_donation": _donation[0]
        }
        donations.append(donation)
        
    return donations

def getPedidos(userConnection,pag = 1):
    mySQL = conection(userConnection)
    mycursor = mySQL.cursor()
    sentence = f"SELECT * FROM pedido LIMIT {(pag-1)*5},5"
    mycursor.execute(sentence)
    donations = mycursor.fetchall()
    mySQL.close()
    return donations

def get5Pedidos(userConnection,pag):
    _orders = getPedidos(userConnection,pag)
    orders = []
    for order in _orders:
        donation = {
            "commune": getCommuneID(userConnection, order[1])[0][2],
            "type": order[2],
            "description": order[3],
            "amount": order[4],
            "name": order[5],
            "id_order": order[0]
        }
        orders.append(donation)
        
    return orders

def getDonationID(userConnection,id):
    mySQL = conection(userConnection)
    mycursor = mySQL.cursor()
    sentence = f"SELECT * FROM donacion WHERE id = {id}"
    mycursor.execute(sentence)
    _donation = mycursor.fetchone()
    _comuna = getCommuneID(userConnection,_donation[1])
    _region = getRegionID(userConnection,_comuna[0][0])
    
    _photos = getPhotos(userConnection,id)
    myDonation ={
        "region": _region[1],
        "commune": _comuna[0][2],
        "calle": _donation[2],
        "typeDonation": _donation[3],
        "amount":_donation[4],
        "date":_donation[5],
        "description":_donation[6],
        "name":_donation[8],
        "email":_donation[9],
        "number":_donation[10],
        "photos":_photos
    }
    
    return myDonation

def getPedidoId(userConnection,id):
    mySQL = conection(userConnection)
    mycursor = mySQL.cursor()
    sentence = f"SELECT * FROM pedido WHERE id = {id}"
    mycursor.execute(sentence)
    _order = mycursor.fetchone()
    _comuna = getCommuneID(userConnection,_order[1])
    _region = getRegionID(userConnection,_comuna[0][0])
    myOrder = {
        "region":_region[1],
        "Commune":_comuna[0][2],
        "type":_order[2],
        "description":_order[3],
        "amount":_order[4],
        "name":_order[5],
        "email":_order[6],
        "number":_order[7]
    }
    return myOrder