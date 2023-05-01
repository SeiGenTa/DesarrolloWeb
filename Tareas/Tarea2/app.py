from flask import Flask, render_template, request

UPLOAD_FOLDER = 'static/svg'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("/menus/initio.html")


@app.route('/agregar_pedido', methods=["GET", "POST"])
def form_add_order():
    if request.method == "GET":
        return render_template("/forms/forms_add.html")

@app.route('/agregar_donacion', methods=["GET", "POST"])
def form_add_don():
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