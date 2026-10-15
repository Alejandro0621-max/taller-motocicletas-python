from flask import Flask, render_template

app = Flask(__name__)

menu_opciones = [
            {"nombre": "Principal", "url": "/Clientes"},
            {"nombre": "Mi moto", "url": "/Clientes/mi-moto"},
            {"nombre": "Mis facturas", "url": "/Clientes/facturas"}
            ]


@app.route("/Clientes")
def index():  
    return render_template('index.html', lista_menu=menu_opciones)

@app.route("/Clientes/mi-moto")
def mimoto():
    return render_template('mimoto.html', lista_menu=menu_opciones)

@app.route("/Clientes/facturas")
def mis_facturas():
    return render_template('mis-facturas.html', lista_menu=menu_opciones)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
