from flask import Flask, render_template, request,redirect, url_for, jsonify
from utils.clases import createDonation, createOrder
from utils.validations import donationValidate, validationOrder
from database.db import getCommune,getRegion,saveDonate, savePhotos, saveOrder, get5Donation

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 13 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HOST = 'localHost'
USER = 'cc5002'
PASSWORD = 'programacionweb'

userConnection = {"HOST":HOST, "USER":USER, "PASSWORD":PASSWORD}

@app.route('/get_regions')
def getRegions():
    return jsonify(getRegion(userConnection))
    
@app.route('/get_communes', methods=['POST'])
def getCommunes():
    var = request.get_json()
    return jsonify(getCommune(userConnection, region = var['inf'])
)
@app.route('/')
def index():
    return render_template("/menus/initio.html");

@app.route('/test', methods=["GET","POST"])
def testing():
    if request.method == "POST":
        print(request.form.get('comunas'))
        return donationValidate(request)
    elif request.method == "GET":
        return "error"


@app.route('/agregar_pedido', methods=["GET", "POST"])
def form_add_order():
    if request.method == "POST":
        '''
        this function validates if the request is correct
        #? return a list, example [true,"complete"] for case in than request is correct
        #!but for incorrect request, return [false,"{reason for error}","{part of request with error}"]
        '''
        valid = validationOrder(request)
        if valid != [True,"complete"]:
            print(valid)
            return render_template("/forms/forms_order.html",data = {"error":valid[1]})
        myOrder = createOrder(request)
        saveOrder(myOrder,userConnection)
        print(valid)
        return redirect(url_for("index"))
    elif request.method == "GET":
        return render_template("/forms/forms_order.html", data = {"error":''})


@app.route('/agregar_donacion', methods=["GET", "POST"])
def form_add_don():
    if request.method == "POST":
        '''
        this function validates if the request is correct
        #? return a list, example [true,"complete"] for case in than request is correct
        #!but for incorrect request, return [false,"{reason for error}","{part of request with error}"]
        '''
        valid = donationValidate(request) 
        if valid != [True,"complete"]:
            print(valid)
            return render_template("/forms/forms_donation.html",data = {"error":valid[1]})
        myDonation = createDonation(request)
        #* this function save the donation in DB and return the donation id 
        idDonation = saveDonate(myDonation,userConnection)
        print(idDonation)
        savePhotos(idDonation,request,userConnection,app.config['UPLOAD_FOLDER'])
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("/forms/forms_donation.html", data = {"error":''})

@app.route('/ver_donaciones/<int:pag>', methods = ["GET"])
def see_donations(pag):
    if request.method == "GET":
        return render_template('/menus/seeDonation.html',pag = pag,data = get5Donation(userConnection,pag =pag))
    
@app.route('/ver_pedidos/<int:pag>', methods = ["GET"])
def see_orders(pag):
    if request.method == "GET":
        return render_template('/menus/seeOrder.html', pag= pag)
    

@app.route('/info_donaciones', methods=["GET"])
def inf_donaciones():
    if request.method == "GET":
        return render_template('/menus/info_donation.html', pag = 1)

@app.route('/info_pedidos', methods=["GET"])
def inf_pedidos():
    if request.method == "GET":
        return render_template('/menus/info_order.html', pag = 1)

if __name__ == "__main__":
    app.run(port=5000,debug=True)
    