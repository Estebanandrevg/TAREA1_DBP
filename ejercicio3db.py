from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from mysql.connector import Error

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:EAvg2356@localhost:3306/dbp12'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)



class Todo(db.Model):   
    __tablename__ = 'Pedidos_Rappy'
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(80), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    pedidos = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Person: {self.id}, {self.direccion}, {self.nombre}, {self.apellido}, {self.pedidos}>'

db.create_all()

@app.route('/create', methods=['POST'])
def create_todo():
    direccion = request.form.get('direccion')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    pedidos = request.form.get('pedidos')
    todo1 = Todo(direccion=direccion,nombre=nombre,apellido=apellido,pedidos=pedidos)
    x=Todo.query.filter_by(id='1').first()
    print(x)
    db.session.add(todo1)
    db.session.commit()
    
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('web.html', data=Todo.query.all())


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True,debug=True, host=('127.0.0.1'))
