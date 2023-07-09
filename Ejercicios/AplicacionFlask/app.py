from flask import Flask, request
from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def calcularIMC():
    peso = int(request.form["txtPeso"])
    altura = float(request.form["txtAltura"])
    imc = peso / (altura * altura)
    print(imc)

    if imc < 18.5:
        mensaje = "Peso Muy Bajo"
    elif imc >= 18.5 and imc < 29.9:
        mensaje = "Peso Normal"
    else:
        mensaje = "Peso Sobrepeso"

    return render_template("index.html", imc=imc, mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
