
import sqlite3
def createdb():
    conn = sqlite3.connect('example.db')

    c = conn.cursor ()
    c.execute('''CREATE TABLE messages
             (who text, message text)''')
    c.execute("INSERT INTO messages VALUES ('admin','helloworld')")
    conn.commit()
    conn.close()

def getdata():
    with sql.connect("example.db") as con:
        cur = con.cursor()
        data = cur.execute('SELECT * FROM messages')
        return data

def insertdata(query):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

createdb()