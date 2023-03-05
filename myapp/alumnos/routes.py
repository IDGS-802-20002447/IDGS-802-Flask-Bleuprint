from flask import Blueprint

#Definimos loas rutas
alumnos=Blueprint("alumnos",__name__)

@alumnos.route("/getalum",methods=["GET"])
def getalum():
    return {"key":"Alumnos"}
