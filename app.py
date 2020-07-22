from flask import Flask, render_template, request, url_for, make_response
import sqlite3

def getdata():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    data = cur.execute('SELECT * FROM messages')

    return data

def insertdata(query):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        who = request.form['who']
        message = request.form['message']


        if(who == "" or message == ""):
            return render_template("index.html")
        insertdata("INSERT INTO messages VALUES ('"+who+"','"+message+"')")
        data = getdata()

        resp = make_response(render_template('index.html',name=who))
        resp.set_cookie('username', who)

        return resp
    if request.method == 'GET':
        name = request.cookies.get('username')

        return render_template("index.html",name=name)

@app.route('/get',methods=['GET', 'POST'])
def getpage():
    data = getdata()
    return render_template("get.html",data=list(data))



app.run(host="0.0.0.0")