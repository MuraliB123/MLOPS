from flask import Flask,render_template,request
import mysql.connector


app = Flask(__name__)


def employee_data(actor_name_var):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'actors'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT actor_Name, Role_of FROM actors_data WHERE actor_Name = %s', (actor_name_var,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results



@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/prediction',methods=['GET','POST'])
def fetch():
    if request.method == 'POST':
        actor_name = request.form['actor_name_var']
        data       = employee_data(actor_name)
        return render_template('index.html',data=data)
       
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')