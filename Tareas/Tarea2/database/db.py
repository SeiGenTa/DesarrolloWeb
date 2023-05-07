import mysql as sql
import mysql.connector
import pymysql as psql
import uuid as uu
import os
from utils.clases import Donation

#* function that put the donation in DB
UPLOAD_FILE = "static/uploads"

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
    #!We going to considerate the donation is valid
    mydb = mysql.connector.connect(host = host,user = user,password = password, database = "tarea2")
    myCursor = mydb.cursor()
    print(f"se guardo la donacion: {donation}")
    myCursor.execute(f"INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES ('{donation.commune_id}',' {donation.address}', '{donation.typeD}','{donation.amount_donation}','{donation.date_available}', '{donation.description}', '{donation.condition}','{donation.name}', '{donation.email}', '{donation.phone_number}')")
    myId = myCursor.lastrowid
    mydb.commit()
    mydb.close()
    return myId

def savePhotos(id_donation:int, request, user:str, password:str, host:str):
    mydb = mysql.connector.connect(host = host,user = user,password = password, database = "tarea2")
    myCursor = mydb.cursor()
    photos = request.files.getlist('fotos')
    for photo in photos:
        name_photo = str(uu.uuid4()) + os.path.splitext(photo.filename)[1].lower() 
        photo.seek(0)
        content_bytes = photo.read()
        print("size",len(photo.read()))
        route_archive = os.path.join(UPLOAD_FILE,name_photo)
        with open(route_archive, "wb") as archive:
            archive.write(content_bytes)
        
        myCursor.execute(f"INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES ('{UPLOAD_FILE}','{name_photo}','{id_donation}')")
        mydb.commit()
        mydb.close()