from flask import Flask, render_template, request, redirect, url_for, flash,g
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import pandas as pd
import numpy as np


app = Flask(__name__)
app.secret_key = "mysecretkey"
DATABASE = 'FuelConsumption.sqlite'
regre={}


def regresion_lineal(): 
    data={
            "coef":0.0,
            "inter":0.0,
            "mean_absolute_error":0.0,
            "mean_squared_error":0.0,
            "root_mean_squared_error":0.0,
            "training":0.0,
            "test":0.0,           
            }
    random_state = 42
    np.random.seed(random_state)
    con = get_db()
    cur = con.cursor()
    df = pd.read_sql_query("SELECT * FROM FuelConsumption",con)
    X, y = df['ENGINESIZE'].values.reshape(-1, 1), df['CO2EMISSIONS'].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_test)
    data["coef"]=np.round(regr.coef_, 2)
    data["inter"]=np.round(regr.intercept_, 2)
    data["mean_absolute_error"]=np.round(mean_absolute_error(y_test, y_pred),2)
    data["mean_squared_error"]=np.round(mean_squared_error(y_test, y_pred),2)
    data["root_mean_squared_error"]=np.round(np.sqrt(mean_squared_error(y_test, y_pred)),2)
    data["training"]=np.round(regr.score(X_train, y_train),2)
    data["test"]=np.round(regr.score(X_test, y_test),2)
    return data
    

def get_db():
    # db = getattr(g, '_database', None)
    # if db is None:
    db =  sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db =  get_db()
    # db = getattr(g, '_database', None)
    # if db is not None:
    db.close()

# settings


# routes
@app.route('/',methods=['GET','POST'])
def Index():
    if request.method == 'POST':
        # cur = get_db().cursor()
        name = request.form['fullname']
        comp_select = request.form.get('comp_select')
        con = get_db()
        cur = con.cursor()
        query='SELECT * FROM FuelConsumption'
        if comp_select != "" and name !="": 
            query='SELECT * FROM FuelConsumption where {} = "{}"'.format(comp_select,name)
        data =cur.execute(query)
        #data = cur.fetchall()
        #close_connection()
        #len(data.description)
        data_regre = regresion_lineal()
        # if data.rowcount != -1: 
        #     return redirect(url_for('index') )
        # else:
        return render_template('index.html', contacts = data, regre = data_regre)
    if request.method == 'GET':
        # cur = get_db().cursor()
        con = get_db()
        cur = con.cursor()
        data =cur.execute('SELECT * FROM FuelConsumption')
        #data = cur.fetchall()
        #close_connection()
        data_regre = regresion_lineal()
        return render_template('index.html', contacts = data, regre = data_regre)





# starting the app
if __name__ == "__main__":
    val = int(input('Desea crear la BD si = 1 ó no = 0'))
    if val==1:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS FuelConsumption')
        f_fuel = open("create_FuelConsumption.sql", "r")
        cur.execute(f_fuel.read())
        f_insert = open("insert_FuelConsumption.sql", "r")
        cur.execute(f_insert.read())
        con.commit()
    app.run(debug=True)
