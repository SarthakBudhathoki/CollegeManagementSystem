import mysql.connector as mc


class Database:
    def __init__(self):
        self.connection = mc.connect(host='localhost', user='root', password='123456', database='course')
        self.cursor = self.connection.cursor()

    def add(self, query=None, values=None):
        self.cursor.execute(query, values)
        self.connection.commit()

    def update(self, query=None, values=None):
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, query=None, values=None):
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch(self, query=None ,value=None):
        self.cursor.execute(query,value)
        row = self.cursor.fetchone()
        return row

    def fetch_all(self, query=None, value=None):
        self.cursor.execute(query, value)
        row = self.cursor.fetchall()
        return row



