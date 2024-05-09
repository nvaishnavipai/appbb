from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'V@!shnavi408'
app.config['MYSQL_DB'] = 'sample_database'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sample_data")
    data = cur.fetchall()
    cur.close()
    return render_template('home.html', data=data)
@app.route('/donormange')
def donormange():
    return render_template('dman.html')

@app.route('/adddonorpage')
def adddonorpage():
    return render_template('and.html')

@app.route('/addrecpage')
def addrecpage():
    return render_template('anr.html')

@app.route('/bloodinv')
def bloodinv():
    return render_template('../static/binv.html')

@app.route('/adddonor',methods=['POST'])
def adddonor():
    name = request.form['name']
    phone = request.form['phone']
    dob = request.form['dob']
    email = request.form['email']
    bloodGroup = request.form['bloodGroup']
    address = request.form['address']
    disease = request.form['disease']
    height = request.form['height']
    weight = request.form['weight']

    cur = mysql.connection.cursor()
    sql = "insert into sample_data (name, phone_number, city, state, country, blood_group, gender,dob,email)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name,phone,"","","",bloodGroup,"",dob,email)
    print(sql)
    print(val)
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()

    return render_template('dman.html')

@app.route('/addrec',methods=['POST'])
def addrec():
    name = request.form['name']
    phone = request.form['phone']
    hospital = request.form['hospital']
    city = request.form['city']
    state = request.form['state']
    country = request.form['country']
    bloodGroup = request.form['bloodGroup']
    gender = request.form['gender']

    cur = mysql.connection.cursor()
    sql = "insert into recipient_data (name, phone_number, hospital_name, city, state, country, blood_group, gender)  values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name,phone,hospital,city,state,country,bloodGroup,gender)
    print(sql)
    print(val)
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.close()

    return render_template('dman.html')

@app.route('/viewdonor')
def viewdonor():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sample_data")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/viewrec')
def viewrec():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM recipient_data")
    data = cur.fetchall()
    cur.close()
    return render_template('viewrec.html', data=data)

@app.route('/elicri')
def elicri():
    return render_template('ec.html')

@app.route('/search',methods=['POST'])
def search():
    search = "%" +request.form['search']  + "%"
    type = request.form['type']
    sql = "select * from sample_data where name like %s OR phone_number like %s OR blood_group like %s"
 
    cur = mysql.connection.cursor()
    val = (search,search,search)
    print("type")
    print(type)
    cur.execute(sql,val)
    data = cur.fetchall()
    print(sql)
    print(ValueError)
    mysql.connection.commit()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/searchrec',methods=['POST'])
def searchrec():
    search = "%" +request.form['search']  + "%"
    type = request.form['type']
    sql = "select * from recipient_data where name like %s OR phone_number like %s OR blood_group like %s"
 
    cur = mysql.connection.cursor()
    val = (search,search,search)
    print("type")
    print(type)
    cur.execute(sql,val)
    data = cur.fetchall()
    print(sql)
    print(ValueError)
    mysql.connection.commit()
    cur.close()
    return render_template('viewrec.html', data=data)

@app.route('/delete/<id>')
def delete(id):
    sql = "delete from sample_data where id = %s"
    cur = mysql.connection.cursor()
    print(id)
    val = (id,)
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.execute("select * from sample_data")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

@app.route('/deleterec/<id>')
def deleterec(id):
    sql = "delete from recipient_data where id = %s"
    cur = mysql.connection.cursor()
    print(id)
    val = (id,)
    cur.execute(sql,val)
    mysql.connection.commit()
    cur.execute("select * from recipient_data")
    data = cur.fetchall()
    cur.close()
    return render_template('viewrec.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

