import mysql.connector

class Database:
    def __init__(self, database_name):
        self.__database_name = database_name

    def setLocalhost(self, localhost):
        self.__localhost = localhost

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setTableMahasiswa(self, table_mahasiswa):
        self.__table_mahasiswa = table_mahasiswa

    def setTableMk(self, table_mk):
        self.__table_mk = table_mk

    def setNilai(self, table_nilai):
        self.__table_nilai = table_nilai

    def createDatabase(self):
        db = mysql.connector.connect(
            host        = self.__localhost,
            user        = self.__username,
            password     = self.__password
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.__database_name)
        return "Database "+self.__database_name+" has been created"

    def createTable(self):
        self.createConnection()
        cursor = self.__db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__table_mahasiswa+"( nim char(9) primary key, name varchar(50))")
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__table_mk+"( kodemtk char(6) primary key, namamtk varchar(50), "
                                                                     "sks tinyint, semester varchar(2))")
        cursor.execute("CREATE TABLE IF NOT EXISTS "+self.__table_nilai+"( nim char(9), kodemtk char(6), na char (1), "
                                                                        "primary key(nim,kodemtk)  )")

        return "Table has been created"

    def createConnection(self):
        db = mysql.connector.connect(
            host        = self.__localhost,
            user        = self.__username,
            password     = self.__password,
            database    = self.__database_name
        )
        self.__db = db
