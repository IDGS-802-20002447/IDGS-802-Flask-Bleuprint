import flask 

from alumnos.routes import alumnos
from maestros.routes import maestros
from directivos.routes import directivos

app=flask.Flask(__name__)
app.config['DEBUG']=True

@app.route("/",methods=["GET"])
def home():
    return flask.jsonify({"principal":"HOME"})

app.register_blueprint(alumnos)
app.register_blueprint(maestros)
app.register_blueprint(directivos)


if __name__=="__main__":
    app.run(debug=True,port=3000)
