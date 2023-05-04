import unittest as un
import random as ra
from random import randint
import os
import requests

os.chdir(os.path.dirname(os.path.abspath(__file__)))

regionsAndCommunes = [
	{
		"NombreRegion": "Arica y Parinacota",
		"comunas": ["Arica", "Camarones", "Putre", "General Lagos"]
	},
	{
		"NombreRegion": "Tarapacá",
		"comunas": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
	},
	{
		"NombreRegion": "Antofagasta",
		"comunas": ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"]
	},
	{
		"NombreRegion": "Atacama",
		"comunas": ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]
	},
	{
		"NombreRegion": "Coquimbo",
		"comunas": ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]
	},
	{
		"NombreRegion": "Valparaíso",
		"comunas": ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]
	},
	{
		"NombreRegion": "Región del Libertador Gral. Bernardo O’Higgins",
		"comunas": ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]
	},
	{
		"NombreRegion": "Región del Maule",
		"comunas": ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"]
	},
	{
		"NombreRegion": "Región de Ñuble",
		"comunas": ["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco", "Bulnes", "Chillán Viejo", "Chillán", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Coihueco", "Ñiquén", "San Carlos", "San Fabián", "San Nicolás"]
	},
	{
		"NombreRegion": "Región del Biobío",
		"comunas": ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío"]
	},
	{
		"NombreRegion": "Región de la Araucanía",
		"comunas": ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"]
	},
	{
		"NombreRegion": "Región de Los Ríos",
		"comunas": ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]
	},
	{
		"NombreRegion": "Región de Los Lagos",
		"comunas": ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]
	},
	{
		"NombreRegion": "Región Aisén del Gral. Carlos Ibáñez del Campo",
		"comunas": ["Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]
	},
	{
		"NombreRegion": "Región de Magallanes y de la Antártica Chilena",
		"comunas": ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antártica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
	},
	{
		"NombreRegion": "Región Metropolitana de Santiago",
		"comunas": ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "Santiago", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
	 }
]

class Tests(un.TestCase):
    def testValidate(self):
        #Files valid
        

        Validfile1 ='./imgTest/Sandia.jpg'
        invalidFile = './imgTest/imgNotValid.jpg'
        with open(Validfile1, 'rb') as f1:
            image1_data = f1.read()
            
        with open(invalidFile, 'rb') as f2:
            image2_data = f2.read()

        #Valid emails
        validEmail = ["cdsex@uchile.cl","almartinez@uchile.cl","seVienenCositas@gmail.com"]
        #invalid emails
        invalidEmail1 = ["cadSex@uchile","alva124","cositas.com"]
        #valid region
        reg1 = list(range(len(regionsAndCommunes)))
        #invalid region
        reg3 = "25"
        reg4 = "27"
        
        #invalid comume
        invComune = "100"

        #valid addres
        calle_number_valid = "Calle 123"
        #invalid addres
        calle_number_invalid = "Calle muy larga que excede los 80 caracteres y por lo tanto no es válida juas juas juas"

        #valid types
        type_donation_valid = "Fruta"
        #invalid type
        type_donation_invalid = "Libros"

        #valid amount 
        cantidad_valid = "20kg"
        #invalid amount
        cantidad_invalid1 = "12341523412palabraalksdjaklsdjakljsfklajflkajdslkajdkladjlajdkasjdaldjakjdlsajkldas"
        cantidad_invalid2 = "mucho"

        # Fechas válidas válid in list
        fechas_validas = ["2022-01-01", "2023-02-28", "2024-12-31"]

        # Fechas inválidas válid in list
        fechas_invalidas = ["22-01-01", "2023-13-28", "2024-12-32"]

        # donaciones válidos válid in list
        donaciones_validas = [
            "Canasta de alimentos básicos",
            "Canasta de frutas y verduras",
            "Canasta para desayuno y merienda"
        ]

        # donaciones inválidos in list
        donaciones_invalidas = [
            "Canasta con alimentos no perecederos, productos de higiene personal y limpieza 123123123",
            "Canasta con alimentos orgánicos y de origen sostenible cultivados localmente 1231241231",
        ]

        #in description use 
        #valid names in list
        validName = [
            "Juan Pérez",
            "Ana Maria Rodríguez",
            "José Luis Torres Gómez",
            "Emma Sánchez de la Cruz"
        ]
        #invalid names in list
        invalidName = "Maria Juana Ana Luisa Perpetua Ramona Jacinta Rodríguez Rodríguez"

        #válid Emails in list
        emails_validos = [
            "usuario@gmail.com",
            "mi.correo_ejemplo-2@hotmail.com",
            "correo_ejemplo_3@ejemplo.com.ar"
        ]

        #invalid Emails válid in list
        emails_invalidos = [
            "correo_ejemplo4@dominio",
            "usuario.con_espacios @gmail.com",
            ".usuario@ejemplo.com",
            "este_es_un_ejemplo_de_correo_electronico_largo_que_no_es_valido_porque_tiene_mas_de_80_caracteres@ejemplo.com"
        ]

        # Valid examples in a list
        valid_numbers = [
            "+56912345678",
            "+56998765432"
        ]

        # Invalid examples in a list
        invalid_numbers = [
            "+5691234567890123456",
            "+56012345678",
            "+569abcde1234"
        ]
        #Caso correctos
        files = [('fotos' , ("fotocorrecta.jpg",image1_data,'image/jpeg') ) ]
        for i in range(100):
            regSelect = reg1[randint(1, len(reg1) - 1)]
            commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
            data = {
                'region': regSelect,
                'comunas': commumeSelect,
                'calle-numero': calle_number_valid,
                'tipoDonacion': type_donation_valid,
                'cantidad':cantidad_valid,
                'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
                'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
                'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
                'name_donante':validName[randint(0, len(validName)-1)],
                'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
                'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
            }

            algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
            self.assertEqual([True,'complete'], algo.json())
        
        #Casos incorrectos:
        #Region mala
        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        data = {
            'region': "Dionasurio",
            'comunas': commumeSelect,
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_valid,
            'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"region isn't valid","Dionasurio"], algo.json())

        regSelect = 100
        commumeSelect =3
        data = {
            'region': regSelect,
            'comunas': commumeSelect,
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_valid,
            'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"region isn't valid",100], algo.json())

        #Comuna mala
        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        data = {
            'region': regSelect,
            'comunas': "500",
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_valid,
            'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"comune isn't valid",500], algo.json())

        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        data = {
            'region': regSelect,
            'comunas': commumeSelect,
            'calle-numero': calle_number_invalid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_valid,
            'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"addres isn't valid",calle_number_invalid], algo.json())
        
        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        data = {
            'region': regSelect,
            'comunas': commumeSelect,
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_invalid,
            'cantidad':cantidad_valid,
            'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"type of donation isn't valid",type_donation_invalid], algo.json())

        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        data = {
            'region': regSelect,
            'comunas': commumeSelect,
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_invalid1,
            'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"amount isn't valid",cantidad_invalid1], algo.json())
        
        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        data = {
            'region': regSelect,
            'comunas': commumeSelect,
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_invalid2,
            'fecha': fechas_validas[randint(0, len(fechas_validas)-1)],
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"amount isn't valid",cantidad_invalid2], algo.json())
        
        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        fecha = fechas_invalidas[randint(0, len(fechas_invalidas)-1)]
        data = {
            'region': regSelect,
            'comunas': commumeSelect,
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_valid,
            'fecha': fecha,
            'descripcion':donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"date isn't valid",fecha], algo.json())

        regSelect = reg1[randint(1, len(reg1) - 1)]
        commumeSelect = randint(1, len(regionsAndCommunes[regSelect])) 
        fecha = fechas_validas[randint(0, len(fechas_invalidas)-1)]
        description = donaciones_invalidas[randint(0, len(donaciones_invalidas)-1)]
        data = {
            'region': regSelect,
            'comunas': commumeSelect,
            'calle-numero': calle_number_valid,
            'tipoDonacion': type_donation_valid,
            'cantidad':cantidad_valid,
            'fecha': fecha,
            'descripcion': description,
            'condiciones': donaciones_validas[randint(0, len(donaciones_validas)-1)],
            'name_donante':validName[randint(0, len(validName)-1)],
            'email_donante':emails_validos[randint(0, len(emails_validos)-1)],
            'number-phone': valid_numbers[randint(0, len(valid_numbers)-1)],
        }

        algo = requests.post("http://127.0.0.1:5000/test",data=data, files = files)
        self.assertEqual([False,"description isn't valid"], algo.json())
        

        pass

    def testCreateClassDonation(self):
        pass


if __name__ == '__main__':
    un.main()
