import mysql as sql
import mysql.connector
import pymysql as psql
#from utils.clases import Donation

#* function that put the donation in DB
'''
def saveDonation(donation:Donation,user:str, password:str, host:str, port:str, number:int) -> None:
    mydb = mysql.connector.connect(host = host,user = user,password = password,database = "donacion")
    mycursos = mydb.cursor()
    mycursos.execute(f"INSERT INTO donacion ()")
    pass
'''

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

print(type(getCommune("root","PinoRojo","localHost")))
