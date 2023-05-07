from flask import request
from datetime import datetime
from database.db import getCommune, getRegion

import re
import os

HOST = 'localHost'
USER = 'root'
PASSWORD = 'PinoRojo'

dataRegion = getRegion(USER,PASSWORD,HOST)


def donationValidate(Myrequest):
    ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
    TYPE_DONATION_VALIDE = {"fruta","verdura","otro"}
    AMOUNT_PHOTOS_MAX = 3
    AMOUNT_PHOTOS_MIN = 1
    SYZE_MAX = 4 * 1024 * 1024 ## Impodremos un maximo de 4 Mb por imagen
    
  

    #Validacion de fotos
    if 'fotos' not in Myrequest.files:
        return [False,"photos isn't existed"] #no viene ningun archivo
    photos = Myrequest.files.getlist('fotos')
    AmountPhotos = len(photos)
    if (AmountPhotos< AMOUNT_PHOTOS_MIN) or (AmountPhotos > AMOUNT_PHOTOS_MAX):
        return [False,"amount photos isn't valid"] #El largo no corresponde  
 
    #Comprobamos que todas las complan nuestros requisitos
    for photo in photos:
        extension = os.path.splitext(photo.filename)[1].lower()
        photo.seek(0)
        sizeo = len(photo.read())
        if photo.content_type not in ALLOWED_MIMETYPES:
            return [False,"type of content isn't valid"] #Revisamos que realmente sea una foto
        
        if sizeo > SYZE_MAX: #Comprobamos que no supere cierto tamaño
            return [False,"syze of photo isn't valid"]
        
        if extension not in ALLOWED_EXTENSIONS:
            return [False,"extension of photo isn't valid"]#Nos aseguramos que sean de los tipos que especificamos 
        if (photo.filename.count('.') != 1):
            return [False,"name of photo isn't valid"]#Con limitar la cantidad de puntos podemos evitar (en parte) que nos ataquen al servidor con SSTI

    #Validacion de region
    reqReg = Myrequest.form.get('region')
    #validamos que sea de la forma que queremos
    try: reqReg = int(reqReg)
    except: 
        return [False,"region isn't valid",reqReg]
    
    valdita = False
    for i in dataRegion:
        if i[0] == reqReg:
            valdita = True
    if not valdita :
        return [False,"region isn't valid",reqReg]
    

    #Validacion de comuna
    reqCom = Myrequest.form.get('comunas')
    try: reqCom = int(reqCom)
    except:
        return [False,"comune isn't valid",reqCom]
    
    dataComune = getCommune(USER,PASSWORD,HOST,region=reqReg)
    
    validate = False
    for i in dataComune:
        if i[1] == reqCom:
            validate = True
    if not validate :
        return [False,"comune isn't valid",reqCom]

    #Validacion de direcion
    reqAddre = Myrequest.form.get('calle-numero')
    if reqAddre == None:
        return [False,"addres isn't valid",reqAddre]
    if len(reqAddre) > 80:
        return [False,"addres isn't valid",reqAddre]
        
    #Validacion de tipo de donacion
    reqType = Myrequest.form.get('tipoDonacion')
    if reqType == None:
        return [False,"type of donation isn't valid",reqType]
    if reqType not in TYPE_DONATION_VALIDE:
        return [False,"type of donation isn't valid",reqType]

    #Validacion de cantidad
    amount = Myrequest.form.get('cantidad')
    if amount == None:
        return [False,"amount isn't valid",amount]
    if not re.match("^[0-9]+[a-zA-Z]{0,3}$",amount):
        return [False,"amount isn't valid",amount]
    if len(amount) > 80:
        return [False,"amount isn't valid",amount]

    #Validacion de fecha
    reqFech = Myrequest.form.get('fecha')
    if reqFech == None:
        return [False,"date isn't valid",reqFech]
    if not re.match("^(\d{4})-(\d{2})-(\d{2})$", reqFech):
        return [False,"date isn't valid",reqFech]

    try:
        fecha = datetime.strptime(reqFech, '%Y-%m-%d')
    except:
        return [False,"date isn't valid",reqFech]

    #validacion de description:
    reqDes = Myrequest.form.get('descripcion')
    if reqDes != None:
        if len(reqDes) > 80:
            return [False,"description isn't valid"]

    #validacion de condicion:
    reqCond = Myrequest.form.get('condiciones')
    if reqCond != None:
        if len(reqCond) > 80:
            return [False,"condition isn't valid"]

    #Validacion de nombre
    reqName = Myrequest.form.get('name_donante')
    if reqName == None: 
        return [False,"name isn't valid"]
    if len(reqName) > 80:
        return [False,"name isn't valid"]

    #Validacion de email
    reqEmail = Myrequest.form.get('email_donante')
    if not re.match("^[a-zA-Z0-9_.ñ-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.ñ]+$",reqEmail):
        return [False,"email isn't valid, email have a ."]
    if len(reqEmail) > 80:
        return [False,"email isn't valid"]

    #Validacion de numero de telefono
    reqNum = Myrequest.form.get('number-phone')
    if not re.match("^\+569\d+$", reqNum):
        print(18)
        return [False,"phone numbert isn't valid"]
    if len(reqNum) > 15:
        return [False,"phone numbert isn't valid"]

    return [True,"complete"]
