import pymysql as psql
import uuid as uu
import os
from utils.clases import Donation,Order

#* function that put the donation in DB

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
        
        print(photosForDonation)
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