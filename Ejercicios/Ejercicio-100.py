import json

datosJSON = {"NOMBRE": "JOSE", "EDAD": 25, "SEXO": "MASCULINO"}

print(datosJSON)

datosJSONString = json.dumps(datosJSON)

print(datosJSONString)
