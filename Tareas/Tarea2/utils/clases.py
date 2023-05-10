import mysql as sql
import mysql.connector
from datetime import datetime

def getIdCommune(region):
	cnx = mysql.connector.connect(user='root', password='PinoRojo', host='LocalHost', database ='tarea2')
	cursos = cnx.cursor()


class Order():
    def __init__(self, region, commune, type_order, description, amount, name, email, number_phone):
        self.region = region
        self.commune = commune
        self.description = description
        self.type_order = type_order
        self.amount = amount
        self.name = name
        self.email = email
        self.number_phone = number_phone
        
    def __str__(self):
        return f"Order(region: {self.region}, commune: {self.commune}, type_order: {self.type_order}, description: {self.description}, amount: {self.amount}, name: {self.name}, email: {self.email}, number_phone: {self.number_phone})"
    
    def get(self):
        return (self.region, self.commune, self.description, self.type_order, self.amount, self.name, self.email, self.number_phone)

class Donation():
	def __init__(self, commune, address, type_donation, amount, date, name, email, phone_number, description = None, condition = None):
		self.commune_id = commune
		self.address = address
		self.typeD = type_donation
		self.amount_donation = amount
		self.date_available = datetime.strptime(date, '%Y-%m-%d')
		self.name = name
		self.email = email
		self.phone_number = phone_number
		self.description = description
		self.condition = condition

	def __str__(self):
		return f"<class donation, commune:{self.commune_id}, addres: {self.address}, type Donation: {self.typeD}, amount of donation: {self.amount_donation}, date: {self.date_available}, name: {self.name}, email: {self.email}, phone number: {self.phone_number}, description: {self.description}, condition: {self.condition}>"

	def get(self):
		return (self.commune_id, self.address,  self.typeD,
          self.amount_donation, self.date_available,self.description ,self.condition,
          self.name,  self.email, self.phone_number)
        
    
#Constructors
def createDonation(request):
    donate = Donation(request.form.get("comunas"), request.form.get("calle-numero"), request.form.get("tipoDonacion"), request.form.get("cantidad"), request.form.get("fecha"), request.form.get("name_donante"), request.form.get("email_donante"), request.form.get("number-phone"),description=request.form.get("descripcion"),condition=request.form.get("condiciones"))
    return donate

def createOrder(request):
    region = request.form.get('region')
    commune = request.form.get('comunas')
    type_order = request.form.get('tipeOrder')
    description = request.form.get('descripcion')
    amount = request.form.get('cantidad')
    name = request.form.get('name')
    email = request.form.get('email')
    number_phone = request.form.get('number-phone')

    return Order(region, commune, type_order, description,amount, name, email, number_phone)

