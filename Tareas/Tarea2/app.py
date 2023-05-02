from flask import Flask, render_template, request,redirect, url_for
from utils.clases import Donation
from utils.validations import donationValidate

app = Flask(__name__)
UPLOAD_FOLDER = 'static/svg'
app.config['MAX_CONTENT_LENGTH'] = 13 * 1024 * 1024


@app.route('/')
def index():
    return render_template("/menus/initio.html")


@app.route('/agregar_pedido', methods=["GET", "POST"])
def form_add_order():
    if request.method == "POST":

        return redirect(url_for("index"))
    elif request.method == "GET":
        return render_template("/forms/forms_add.html")


@app.route('/agregar_donacion', methods=["GET", "POST"])
def form_add_don():
    if request.method == "POST":
        #esta funcion valida si el request es correcto, si no es asi retorna un False con el error
        valid = donationValidate(request) 
        if valid != True:
            return render_template("/forms/forms_donation.html",error = valid[1])
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("/forms/forms_donation.html")



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