from flask import Blueprint

#Definimos loas rutas
directivos=Blueprint("directivos",__name__)

@directivos.route("/getDir",methods=["GET"])
def getDir():
    return {"key":"Directivos"}
