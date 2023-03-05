from flask import Blueprint

#Definimos loas rutas
maestros=Blueprint("maestros",__name__)

@maestros.route("/getmaestro",methods=["GET"])
def getmaestro():
    return {"key":"Maestros"}
