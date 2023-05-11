from flask import request
from datetime import datetime
from database.db import getCommune, getRegion

import re
import os

HOST = 'localHost'
USER = 'cc5002'
PASSWORD = 'programacionweb'

dataRegion = getRegion(USER,PASSWORD,HOST)
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}
ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
TYPE_DONATION_VALIDE = {"fruta","verdura","otro"}
AMOUNT_PHOTOS_MAX = 3
AMOUNT_PHOTOS_MIN = 1
SYZE_MAX = 4 * 1024 * 1024 ## Impodremos un maximo de 4 Mb por imagen

def donationValidate(Myrequest):
    #Validacion de fotos
    if 'fotos' not in Myrequest.files:
        return [False,"photos is not existed"] #no viene ningun archivo
    photos = Myrequest.files.getlist('fotos')
    AmountPhotos = len(photos)
    if (AmountPhotos< AMOUNT_PHOTOS_MIN) or (AmountPhotos > AMOUNT_PHOTOS_MAX):
        return [False,"amount photos is not valid"] #El largo no corresponde  
 
    #Comprobamos que todas las complan nuestros requisitos
    for photo in photos:
        extension = os.path.splitext(photo.filename)[1].lower()
        photo.seek(0)
        sizeo = len(photo.read())
        print("size", sizeo)
        if photo.content_type not in ALLOWED_MIMETYPES:
            return [False,"type of content is not valid"] #Revisamos que realmente sea una foto
        
        if sizeo > SYZE_MAX: #Comprobamos que no supere cierto tamaño
            return [False,"syze of photo is not valid"]
        
        if extension not in ALLOWED_EXTENSIONS:
            return [False,"extension of photo is not valid"]#Nos aseguramos que sean de los tipos que especificamos 
        if (photo.filename.count('.') != 1):
            return [False,"name of photo is not valid"]#Con limitar la cantidad de puntos podemos evitar (en parte) que nos ataquen al servidor con SSTI

    #Validacion de region
    reqReg = Myrequest.form.get('region')
    #validamos que sea de la forma que queremos
    try: reqReg = int(reqReg)
    except: 
        return [False,"region is not valid",reqReg]
    
    valdita = False
    for i in dataRegion:
        if i[0] == reqReg:
            valdita = True
    if not valdita :
        return [False,"region is not valid",reqReg]
    

    #Validacion de comuna
    reqCom = Myrequest.form.get('comunas')
    try: reqCom = int(reqCom)
    except:
        return [False,"comune is not valid",reqCom]
    
    dataComune = getCommune(USER,PASSWORD,HOST,region=reqReg)
    
    validate = False
    for i in dataComune:
        if i[1] == reqCom:
            validate = True
    if not validate :
        return [False,"comune is not valid",reqCom]

    #Validacion de direcion
    reqAddre = Myrequest.form.get('calle-numero')
    if reqAddre == None:
        return [False,"addres is not valid",reqAddre]
    if len(reqAddre) > 80:
        return [False,"addres is not valid",reqAddre]
        
    #Validacion de tipo de donacion
    reqType = Myrequest.form.get('tipoDonacion')
    if reqType == None:
        return [False,"type of donation is not valid",reqType]
    if reqType not in TYPE_DONATION_VALIDE:
        return [False,"type of donation is not valid",reqType]

    #Validacion de cantidad
    amount = Myrequest.form.get('cantidad')
    if amount == None:
        return [False,"amount is not valid",amount]
    if not re.match("^[0-9]+[a-zA-Z]{0,3}$",amount):
        return [False,"amount is not valid",amount]
    if len(amount) > 80:
        return [False,"amount is not valid",amount]

    #Validacion de fecha
    reqFech = Myrequest.form.get('fecha')
    if reqFech == None:
        return [False,"date is not valid",reqFech]
    if not re.match("^(\d{4})-(\d{2})-(\d{2})$", reqFech):
        return [False,"date is not valid",reqFech]

    try:
        fecha = datetime.strptime(reqFech, '%Y-%m-%d')
    except:
        return [False,"date is not valid",reqFech]

    #validacion de description:
    reqDes = Myrequest.form.get('descripcion')
    if reqDes != None:
        if len(reqDes) > 80:
            return [False,"description is not valid"]

    #validacion de condicion:
    reqCond = Myrequest.form.get('condiciones')
    if reqCond != None:
        if len(reqCond) > 80:
            return [False,"condition is not valid"]

    #Validacion de nombre
    reqName = Myrequest.form.get('name_donante')
    if reqName == None: 
        return [False,"name is not valid"]
    if len(reqName) > 80:
        return [False,"name is not valid"]

    #Validacion de email
    reqEmail = Myrequest.form.get('email_donante')
    if not re.match("^[a-zA-Z0-9_.ñ-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.ñ]+$",reqEmail):
        return [False,"email is not valid, email have a ."]
    if len(reqEmail) > 80:
        return [False,"email is not valid"]

    #Validacion de numero de telefono
    reqNum = Myrequest.form.get('number-phone')
    if not re.match("^\+569\d{8}$", reqNum):
        print(18)
        return [False,"phone numbert is not valid"]
    if len(reqNum) > 15:
        return [False,"phone numbert is not valid"]

    return [True,"complete"]

###VALIDACION DE PEDIDO
def validationOrder(myResquest):
    #Validacion de region
    reqReg = myResquest.form.get('region')
    #validamos que sea de la forma que queremos
    try: reqReg = int(reqReg)
    except: 
        return [False,"region is not valid",reqReg]
    
    valdita = False
    for i in dataRegion:
        if i[0] == reqReg:
            valdita = True
    if not valdita :
        return [False,"region is not valid",reqReg]
    

    #Validacion de comuna
    reqCom = myResquest.form.get('comunas')
    try: reqCom = int(reqCom)
    except:
        return [False,"comune is not valid",reqCom]
    
    dataComune = getCommune(USER,PASSWORD,HOST,region=reqReg)
    
    validate = False
    for i in dataComune:
        if i[1] == reqCom:
            validate = True
    if not validate :
        return [False,"comune is not valid",reqCom]
        
    #Validacion de tipo de donacion
    reqType = myResquest.form.get('tipeOrder')
    if reqType == None:
        return [False,"type of donation is not valid",reqType]
    if reqType not in TYPE_DONATION_VALIDE:
        return [False,"type of donation is not valid",reqType]

    #validacion de description:
    reqDes = myResquest.form.get('descripcion')
    if reqDes == None:
        return [False,"description is not valid"]
    if len(reqDes) > 250:
        return [False,"description is not valid"]
    
    #Validacion de cantidad
    amount = myResquest.form.get('cantidad')
    if not re.match("^[0-9]+[a-zA-Z]{0,3}$",amount):
        return [False,"amount is not valid",amount]
    if len(amount) > 80:
        return [False,"amount is not valid",amount]

    reqName = myResquest.form.get('name')
    if reqName == None: 
        return [False,"name is not valid"]
    if len(reqName) > 80:
        return [False,"name is not valid"]
    
    #Validacion de email
    reqEmail = myResquest.form.get('email')
    if not re.match("^[a-zA-Z0-9_.ñ-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.ñ]+$",reqEmail):
        return [False,"email is not valid, email have a ."]
    if len(reqEmail) > 80:
        return [False,"email is not valid"]
    
    #Validacion de numero de telefono
    reqNum = myResquest.form.get('number-phone')
    if reqNum != '':
        if not re.match("^\+569\d{8}$", reqNum):
            print(18)
            return [False,"phone numbert is not valid"]
        if len(reqNum) > 15:
            return [False,"phone numbert is not valid"]

    return [True,"complete"]