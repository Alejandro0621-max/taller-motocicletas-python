from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)

data = {
    "titulo":"App de Gestion",
    "bienvenida":"¡Saludos!"
}

paginas = {
    "factura": "Facturación",
    "orden_servicio": "Orden de Servicio",
    "clientes": "Clientes",
    "motos": "Motocicletas",
    "inventario": "Inventario",
    "servicios" : "Servicios",
    "/" : "Salir"
}



@app.context_processor
def inject_menu():
    return dict(lista_menu=paginas)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<pagina>")
def ver_pagina(pagina):
    if pagina not in paginas:
        abort(404)

    return render_template(
        f"{pagina}.html",
        pagina_actual=pagina,
        lista_menu=paginas
    )
@app.route("/crear_factura")
def crear_factura():
    return render_template("crear_factura.html")

@app.route("/crear_orden")
def crear_orden():
    return render_template("crear_orden.html")

if __name__ =="__main__":
    app.run(debug=True, port=5000)