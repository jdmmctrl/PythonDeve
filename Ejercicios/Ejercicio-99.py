import json

datos = '{"nombre":"Juan","edad":30, "ciudad":"Bogota", "pais":"Colombia}'

print(datos)

lecturaDatos = json.loads(datos)

print(lecturaDatos["nombre"])
