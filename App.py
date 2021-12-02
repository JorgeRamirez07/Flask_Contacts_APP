from flask import Flask, render_template,request,redirect,url_for,session,flash
from flask.globals import request
from werkzeug.exceptions import PreconditionRequired
from flask_mysqldb import MySQL

#Congig MySQL
app = Flask(__name__,template_folder='Template')
app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_USER'] = 'bcd79f7861ec0d'
app.config['MYSQL_PASSWORD'] = '5154a512'
app.config['MYSQL_DB'] = 'heroku_74bc1e07cc53dc3'
#init MySQL
mysql = MySQL(app)

#semilla para encriptamiento



##define la ruta para ingresar


@app.route('/Registro')
def redireccionRegis():
   # cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM usuario")
    #data = cur.fetchall()

    return render_template("Registrar.html")

@app.route('/GuardarRegistro',methods = ['POST'])
def registrar():
         #obtiene los datos
       
        name = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        typetel = request.form['typetel']
        numtel = request.form['numtel']
        doc = request.form['doc']
        numdoc = request.form['numdoc']
        adress = request.form['adress']
        user = request.form['userlogin']
        password = request.form['PasswLogin']
        rol = request.form['rol']
        estado = request.form['estado']
        print("Insertado")
        cur = mysql.connection.cursor()
        #Prepara query para insercion
        cur.execute("INSERT into usuario(Nombres,Apellidos,Edad,Telefono,Numero_telefono,Documento,Numero_Doc,Direccion,Username,Contraseña,Rol,Estado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (name,lastname,age,typetel,numtel,doc,numdoc,adress,user,password,rol,estado))
        #Crear Cursos
        mysql.connection.cursor()
        #Ejecutar Query
       
        
        #commit a BD
        mysql.connection.commit()
        print(user)
        print(rol)
        print(estado)
        

        return render_template('index.html')
@app.route('/add_specie',methods = ['POST'])
def add_race():
        name = request.form['name']
        #size = request.form['size']
        #species = request.form['species']
        estado = request.form['estado']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO especie (Nombre,estado) VALUES(%s,%s)',
        (name,estado))
        mysql.connection.commit()
        print(name)
       
        return redirect(url_for('Index'))
@app.route('/',methods=["GET","POST"])
def Index():
    if(request.method=="GET"):
        if'name' in session:
            #carga template 
            return render_template('inicio.html')
            #Accesso no concedido 
        else:
            print("Aquí")
            return render_template('index.html')
    else:
        #obtiene los datos
        user = request.form['userlogin']
        password = request.form['PasswLogin']

@app.route('/InicioSesion',methods =["GET"])
def pagAdmin():
    if(request.method=="GET" ):
        if'name' in session:
            #carga template 
            return render_template('inicio.html')
            #Accesso no concedido 
        else:
            print("Aquí")
          #  return render_template('index.html')
    else:
        #obtiene los datos
        user = request.form['userlogin']
        password = request.form['PasswLogin']
    return render_template("SitioAdmin.html")

@app.route('/InicioSesionUser',methods =["GET"])
def pagUsuario():
    if(request.method=="GET"  ):
        
   
        #obtiene los datos
        user = request.form['userlogin']
        password = request.form['PasswLogin']
        return render_template("SitioUsuario.html")

@app.route('/edit')
def edit_contact():
    return 'edit contact'
    
@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True) 