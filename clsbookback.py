import mysql.connector
from mysql.connector import errorcode

class dbbooks:

    def __init__(self):
        conn = self.create_conn()
        cur = conn.cursor()

#        db = 'pyBase'
        TABLES = {}

        TABLES['titles'] = (
            "CREATE TABLE `books` ("
            "  `idtitle` INT(11) NOT NULL AUTO_INCREMENT,"
            "  `title` VARCHAR(75),"
            "  `author` VARCHAR(25) NOT NULL,"
            "  `year` INT(4),"
            "  `ISBN` BIGINT(13),"
            "  PRIMARY KEY (`idtitle`)"
            ") ENGINE=InnoDB")

        for name, ddl in TABLES.items():
            try:
                print("Creating table {}: ".format(name), end='')
                cur.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        cur.close()
        conn.close()

    def create_conn(self):
        from socket import gethostname

        config = {
            'user': 'dmontysql',
            'password': '37Sunrise' if gethostname() == 'mint18' else 'sun37rIse',
            'host': 'us1604' if gethostname() == 'mint18' else 'kermit',
            'db': 'pyBase',
            'raise_on_warnings': True,
        }

        try:
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return
        else:
            return cnx

    def insert(self, title, author, year, isbn):
        conn = self.create_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, year, isbn)"
                    " VALUES(%s,%s,%s,%s)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = self.create_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        conn = self.create_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE title=%s OR author=%s OR year=%s OR isbn =%s", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def update(self, idtitle, title, author, year, isbn):
        conn = self.create_conn()
        cur = conn.cursor()
        print("UPDATE books SET title = %s, author = %s, year = %s, isbn = %s WHERE idtitle = %s " % (
        title, author, year, isbn, idtitle))
        try:
            cur.execute("UPDATE books SET title = %s, author = %s, year = %s, isbn = %s WHERE idtitle = %s",
                        (title, author, year, isbn, idtitle))
        except mysql.connector.Error as err:
            print(err, err.errno)
        else:
            print("OK")
        conn.commit()
        conn.close()

    def delete(self, item):
        conn = self.create_conn()
        cur = conn.cursor()
        print("DELETE FROM books WHERE idtitle={}".format(item))
        cur.execute("DELETE FROM books WHERE idtitle={}".format(item))
        conn.commit()
        conn.close()
