import mysql as sql
import mysql.connector
import pymysql as psql
import uuid as uu
import os
from utils.clases import Donation,Order

#* function that put the donation in DB


def getRegion(user:str, password:str, host:str):
    mydb = mysql.connector.connect(host = host,user = user,password = password,database = "tarea2")
    mycursos = mydb.cursor()
    mycursos.execute(f"SELECT id, nombre FROM region")
    data = mycursos.fetchall()
    mycursos.close()
    mydb.close()
    return data

def getCommune(user:str, password:str, host:str, region:int = None):
    mydb = mysql.connector.connect(host = host,user = user,password = password, database = "tarea2")
    mycursos = mydb.cursor()
    if region == None:
        mycursos.execute(f"SELECT region_id ,id , nombre FROM comuna")
    else:
        mycursos.execute(f"SELECT region_id ,id , nombre FROM comuna WHERE region_id = {str(region)}")
    data = mycursos.fetchall()
    mycursos.close()
    mydb.close()
    return data

def saveDonate(donation:Donation,user:str, password:str, host:str):
    #!We will to considerate the donation is valid
    mydb = mysql.connector.connect(host = host,user = user,password = password, database = "tarea2")
    myCursor = mydb.cursor()
    myCursor.execute(f"INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES ('{donation.commune_id}',' {donation.address}', '{donation.typeD}','{donation.amount_donation}','{donation.date_available}', '{donation.description}', '{donation.condition}','{donation.name}', '{donation.email}', '{donation.phone_number}')")
    myId = myCursor.lastrowid
    mydb.commit()
    mydb.close()
    return myId

def savePhotos(id_donation:int, request, user:str, password:str, host:str,UPLOAD_FILE = "static/uploads"):
    mydb = mysql.connector.connect(host = host,user = user,password = password, database = "tarea2")
    myCursor = mydb.cursor()
    photos = request.files.getlist('fotos')
    for photo in photos:
        _fileName = str(uu.uuid4()) + os.path.splitext(photo.filename)[1].lower() 
        photo.seek(0)
        _ContentBytes = photo.read()
        routeNewFile = os.path.join(UPLOAD_FILE,_fileName)
        with open(routeNewFile, "wb") as archive:
            archive.write(_ContentBytes)
        
        myCursor.execute(f"INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES ('{UPLOAD_FILE}','{_fileName}','{id_donation}')")
        mydb.commit()
    mydb.close()
    
def saveOrder(order:Order,user:str, password:str, host:str):
    mydb = mysql.connector.connect(host = host,user = user,password = password, database = "tarea2")
    myCursor = mydb.cursor()
    sentence = f"INSERT INTO pedido (comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES ("
    save = f'"{order.commune}","{order.type_order}","{order.description}","{order.amount}","{order.name}","{order.email}","{order.number_phone}"'
    myCursor.execute(sentence+save+")")
    mydb.commit()
    mydb.close()
    
def getDonation(user:str, password:str, host:str, pag = 1):
    mydb = mysql.connector.connect(host = host,user = user,password = password, database = "tarea2")
    myCursor = mydb.cursor()
    sentence = f"SELECT * FROM donacion LIMIT {(pag-1)*5},5"
    myCursor.execute(sentence)
    donations = myCursor.fetchall()
    print(donations[1])
    
def getPhotos(idUser):
    pass