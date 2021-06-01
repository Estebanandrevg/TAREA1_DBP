from threading import Semaphore
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from mysql.connector import Error

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:EAvg2356@localhost:3306/dbp12'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)



class profesor(db.Model):   #creo una tabla 'profesor' en mi base de datos.
    __tablename__ = 'profesor'
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(80), nullable=False)
    Apellido = db.Column(db.String(80), nullable=False)
    Materia = db.Column(db.String(80), nullable=False)
    Experiencia = db.Column(db.Integer)

    def __repr__(self):
        return f'<profesor: {self.id}, {self.Nombre}, {self.Apellido}, {self.Materia}, {self.Experiencia}>'



class estudiante(db.Model):   #creo una tabla 'estudiante' en mi base de datos.
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(80), nullable=False)
    Dificultad = db.Column(db.Integer)
    TRIKA = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<estudiante: {self.id}, {self.Nombre},{self.Dificultad}, {self.TRIKA}>'



class curso(db.Model):   #creo una tabla 'curso' en mi base de datos.
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    Letra = db.Column(db.String(80), nullable=False)
    Nombre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<curso: {self.id}, {self.Letra}, {self.Nombre}>'



class sección(db.Model):   #creo una tabla 'sección' en mi base de datos.   
    __tablename__ = 'sección'
    id = db.Column(db.Integer, primary_key=True)
    Letra = db.Column(db.String(80), nullable=False)
    Nombre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<sección: {self.id}, {self.Letra}, {self.Nombre}>'



db.create_all() #detecta modelos y crea tablas si no existen


@app.route('/')
def index():
    return 'Inicio'

@app.route('/profesor')
def profesor_nombre():
    return "________\n".join([p.Nombre for p in profesor.query.all()]) + "<p>"+"________\n".join([p.Apellido for p in profesor.query.all()]) + "<p>"+"________\n".join([p.Materia for p in profesor.query.all()]) + "<p>"+"________\n".join([str(p.Experiencia) for p in profesor.query.all()])  

@app.route('/estudiante')
def profesor_apellido():
     return "________\n".join([p.Nombre for p in estudiante.query.all()]) + "<p>"+"________\n".join([str(p.Dificultad) for p in estudiante.query.all()]) + "<p>"+"________\n".join([str(p.TRIKA) for p in estudiante.query.all()])  

@app.route('/curso')
def profesor_materia():
    return "________\n".join([p.Letra for p in curso.query.all()]) + "<p>"+"________\n".join([p.Nombre for p in curso.query.all()])

@app.route('/sección')
def profesor_experiencia():
    return "________\n".join([p.Letra for p in sección.query.all()]) + "<p>"+"________\n".join([p.Nombre for p in sección.query.all()]) 




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True,debug=True, host=('127.0.0.1'))
else:
    print('using global variables from FLASK')