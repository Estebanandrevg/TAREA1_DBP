import psycopg2

connection = psycopg2.connect('dbname=postgres user=postgres password=1234')
#se crea una sesion por la conección

cursor = connection.cursor()

cursor.execute('drop table if exists profesor;') 
cursor.execute('drop table if exists estudiante;') 
cursor.execute('drop table if exists curso;') 
cursor.execute('drop table if exists seccion;') 

cursor.execute(''' 
    create table profesor(
        id INTEGER PRIMARY KEY,
        Nombre VARCHAR(40) NOT NULL,
        Apellido VARCHAR(40) NOT NULL,
        Materia VARCHAR(40) NOT NULL,
        Experiencia INT 
    )
''')

cursor.execute(''' 
    create table estudiante(
        id INTEGER PRIMARY KEY,
        Nombre VARCHAR(40) NOT NULL,
        Año INT,
        TRIKA BOOLEAN NOT NULL DEFAULT False
    )
''')

cursor.execute(''' 
    create table curso(
        id INTEGER PRIMARY KEY,
        Nombre VARCHAR(40) NOT NULL,
        Dificultad INT
    )
''')


cursor.execute(''' 
    create table seccion(
        id INTEGER PRIMARY KEY,
        Letra VARCHAR(40) NOT NULL,
        Nombre VARCHAR(40) NOT NULL
    )
''')

#tabla del profesor
data_profesor1 = {'id':1, 'Nombre': "Geraldo",'Apellido': "Quizpe",'Materia':"Matematica_I",'Experiencia':35}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor1)

data_profesor2 = {'id':2, 'Nombre': "Alberto",'Apellido': "Gonzales",'Materia':"Fisica_I",'Experiencia':27}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor2)

data_profesor3 = {'id':3, 'Nombre': "Joaquin",'Apellido': "del Campo",'Materia':"POOII",'Experiencia':22}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor3)

data_profesor4 = {'id':4, 'Nombre': "Sebastian",'Apellido': "Garcia",'Materia':"Matematica_II",'Experiencia':18}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor4)

data_profesor5 = {'id':5, 'Nombre': "Juan",'Apellido': "Perez",'Materia':"Fisica_II",'Experiencia':15}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor5)

data_profesor6 = {'id':6, 'Nombre': "Antonio",'Apellido': "Barroso",'Materia':"Lenguaje",'Experiencia':13}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor6)

data_profesor7 = {'id':7, 'Nombre': "Arturo",'Apellido': "Morales",'Materia':"Historia",'Experiencia':10}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor7)

data_profesor8 = {'id':8, 'Nombre': "Benito",'Apellido': "Vargas",'Materia':"Filosofia",'Experiencia':10}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor8)

data_profesor9 = {'id':9, 'Nombre': "Santiago",'Apellido': "Sandoval",'Materia':"Letras",'Experiencia':8}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor9)

data_profesor10 = {'id':10, 'Nombre': "Luana",'Apellido': "Cruz",'Materia':"DBP",'Experiencia':6}
SQL_INSERT= 'insert into profesor(id, Nombre,Apellido,Materia,Experiencia) values(%(id)s, %(Nombre)s, %(Apellido)s, %(Materia)s, %(Experiencia)s);'
cursor.execute(SQL_INSERT,data_profesor10)



#tabla del estudiante
data_estudiante1 = {'id':1, 'Nombre': "Marco",'Año': 5,'TRIKA':False}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante1)

data_estudiante2 = {'id':2, 'Nombre': "Antonela",'Año': 5,'TRIKA':True}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante2)

data_estudiante3 = {'id':3, 'Nombre': "Gabriel",'Año': 5,'TRIKA':False}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante3)

data_estudiante4 = {'id':4, 'Nombre': "Lynet",'Año': 5,'TRIKA':False}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante4)

data_estudiante5 = {'id':5, 'Nombre': "Andrea",'Año': 4,'TRIKA':True}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante5)

data_estudiante6 = {'id':6, 'Nombre': "Diego",'Año': 4,'TRIKA':True}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante6)

data_estudiante7 = {'id':7, 'Nombre': "Matias",'Año': 3,'TRIKA':False}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante7)

data_estudiante8 = {'id':8, 'Nombre': "Victoria",'Año': 2,'TRIKA':False}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante8)

data_estudiante9 = {'id':9, 'Nombre': "Alejandro",'Año': 2,'TRIKA':False}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante9)

data_estudiante10 = {'id':10, 'Nombre': "Victor",'Año': 1,'TRIKA':True}
SQL_INSERT= 'insert into estudiante(id, Nombre,Año,TRIKA) values(%(id)s, %(Nombre)s, %(Año)s, %(TRIKA)s);'
cursor.execute(SQL_INSERT,data_estudiante10)



#tabla del curso
data_curso1 = {'id':1, 'Nombre': "Matematica_II",'Dificultad': 10}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso1)

data_curso2 = {'id':2, 'Nombre': "Fisica_II",'Dificultad': 10}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso2)

data_curso3 = {'id':3, 'Nombre': "Matematica_I",'Dificultad': 9}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso3)

data_curso4 = {'id':4, 'Nombre': "Fisica_I",'Dificultad': 7}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso4)

data_curso5 = {'id':5, 'Nombre': "DBP",'Dificultad': 6}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso5)

data_curso6 = {'id':6, 'Nombre': "Lenguaje",'Dificultad': 5}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso6)

data_curso7 = {'id':7, 'Nombre': "Historia",'Dificultad': 5}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso7)

data_curso8 = {'id':8, 'Nombre': "Filosofia",'Dificultad': 4}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso8)

data_curso9 = {'id':9, 'Nombre': "Letras",'Dificultad': 2}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso9)

data_curso10 = {'id':10, 'Nombre': "POOII",'Dificultad': 2}
SQL_INSERT= 'insert into curso(id, Nombre, Dificultad) values(%(id)s, %(Nombre)s, %(Dificultad)s);'
cursor.execute(SQL_INSERT,data_curso10)



#tabla del seccion
data_seccion1 = {'id':1, 'Letra': "A",'Nombre': 'HelpFull'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion1)

data_seccion2 = {'id':2, 'Letra': "B",'Nombre': 'Kind'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion2)

data_seccion3 = {'id':3, 'Letra': "B",'Nombre': 'Kind'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion3)

data_seccion4 = {'id':4, 'Letra': "C",'Nombre': 'Fair'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion4)

data_seccion5 = {'id':5, 'Letra': "C",'Nombre': 'Fair'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion5)

data_seccion6 = {'id':6, 'Letra': "C",'Nombre': 'Fair'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion6)

data_seccion7 = {'id':7, 'Letra': "D",'Nombre': 'Loyal'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion7)

data_seccion8 = {'id':8, 'Letra': "D",'Nombre': 'Loyal'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion8)

data_seccion9 = {'id':9, 'Letra': "E",'Nombre': 'Honest'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion9)

data_seccion10 = {'id':10, 'Letra': "E",'Nombre': 'Honest'}
SQL_INSERT= 'insert into seccion(id, Letra, Nombre) values(%(id)s, %(Letra)s, %(Nombre)s);'
cursor.execute(SQL_INSERT,data_seccion10)


print(' ')
print('Tabla de profesores:')
print(' ')

cursor.execute('select * from profesor;') 
for i in range(1,10):
    x = cursor.fetchmany(1)
    print(x)

print(' ')
print('Tabla de Estudiantes:')
print(' ')

cursor.execute('select * from estudiante;') 
for i in range(1,10):
    x = cursor.fetchmany(1)
    print(x)

print(' ')
print('Tabla de Cursos:')
print(' ')

cursor.execute('select * from curso;') 
for i in range(1,10):
    x = cursor.fetchmany(1)
    print(x)

print(' ')
print('Tabla de Secciones:')
print(' ')

cursor.execute('select * from seccion;') 
for i in range(1,10):
    x = cursor.fetchmany(1)
    print(x)
    
print(' ')
print(' ')
print(' ')


connection.commit()
connection.close()
connection.close()