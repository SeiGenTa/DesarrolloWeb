import mysql as sql
import mysql.connector

def getIdCommune(region):
	cnx = mysql.connector.connect(user='root', password='PinoRojo', host='LocalHost', database ='tarea2')
	cursos = cnx.cursor()



class Donation():
	def __init__(self, region, comuna, addres, type_donation, amount, date, photos, name, email, phone_number, description = None, condition = None):
		self.region = region
		self.comuna = comuna
		self.addres = addres
		self.typeD = type_donation
		self.amount_donation = amount
		self.date = date
		self.photos = photos
		self.name = name
		self.email = email
		self.phone_number = phone_number
		self.description = description
		self.condition = condition

	def __str__(self):
		return f"<class donation: region:{self.region}, commune:{self.comuna}, addres: {self.addres}, type Donation: {self.typeD}, amount of donation: {self.amount_donation}, date: {self.date}, photos: {self.photos}, name: {self.name}, email: {self.email}, phone number: {self.phone_number}, description: {self.description}, condition: {self.condition}"

	def get(self):
		return (self.region, self.comuna, self.addres,  self.typeD, self.amount_donation, self.date, self.photos,
        	 self.name,  self.email, self.phone_number ,self.description ,self.condition)
		#return {'region': self.region,'commune': self.comuna,'addres': self.addres, 'tipeDonation': self.typeD,'amountDonation':self.amount_donation, 'date': self.date, 'photos':self.photos,
        #  	'name': self.name, 'email': self.email, 'phoneNumber':self.phone_number ,'description':self.description ,'condition':self.condition}
        
#Constructors
def donation(request):
    donate = Donation(request.form.get("region"), request.form.get("comunas"), request.form.get("calle-numero"), request.form.get("tipoDonacion"), request.form.get("cantidad"), request.form.get("fecha"), request.files.getlist("fotos"), request.form.get("name_donante"), request.form.get("email_donante"), request.form.get("number-phone"),description=request.form.get("descripcion"),condition=request.form.get("condiciones"))
    return donate

