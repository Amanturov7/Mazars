
import mysql.connector

# Create the connection object
from mysql.connector import Error

myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456789", database="sys")

# creating the cursor object
cur = myconn.cursor()
def start(id):
    try:
        cur.execute("select * from books where id="+id)

        result = cur.fetchall()

        for x in result:
            print(x)
            return x
    except:
        myconn.rollback()

def getAll():
    try:
        cur.execute("select * from sys.books")

        result = cur.fetchall()

        return result
    except:
        myconn.rollback()

def delete(id):

        query = "DELETE FROM books WHERE id = %s"

        try:

            cursor = myconn.cursor()
            cursor.execute(query, (id,))

            myconn.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            myconn.close()


def create(id,isbn,name,author,section):
    sql = "insert into books(id,isbn,Name,Author,Section) values(%s, %s, %s, %s, %s)"

    val = (id, isbn, name, author, section)

    try:
            cursor = myconn.cursor()
            cursor.execute(sql, val)

            myconn.commit()
    except:
        myconn.rollback()

        cursor.close()
        myconn.close()

def update(id,isbn,name,author,section):
    # sql = "UPDATE books SET isbn="+isbn+" name="+name+" Author="+author+" Section="+section+" WHERE id ="+id+";"
    sql = "UPDATE sys.books SET isbn= %s, name= %s, Author= %s, Section= %s WHERE id = %s;"

    val = (isbn, name, author, section,id)

    try:

            cursor = myconn.cursor()
            cursor.execute(sql,val)

            myconn.commit()
    except:

        cursor.close()
        myconn.close()
