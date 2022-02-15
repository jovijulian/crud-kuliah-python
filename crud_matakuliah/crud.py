import mysql.connector

class CRUD:

	def __init__(self):
		self.__localhost     = "localhost"
		self.__username      = "root"
		self.__password      = ""
		self.__database_name = "python_crud_kuliah"
		self.__table_name 	 = "matakuliah"
		self.createConnection()

	def create(self):
		print('Input kode mata kuliah: ')
		kodemtk = input()
		print('Input nama mata kuliah: ')
		namamtk = input()
		print('Input SKS: ')
		sks = input()
		print('Input semester: ')
		semester = input()

		cursor = self.__db.cursor()

		val = (kodemtk, namamtk, sks, semester)
		cursor.execute("INSERT INTO "+self.__table_name+" (kodemtk, namamtk, sks, semester) VALUES (%s, %s, %s, %s)", val)

		self.__db.commit()

		print(cursor.rowcount, "record inserted.")

	def read(self):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+"")

		myresult = cursor.fetchall()

		for x in myresult:
		  print(x)

	def update(self):
		print('Search by kode mata kuliah:')
		kodemtk = input()

		print('Edit nama mata kuliah:')
		namamtk = input()

		if namamtk == "":
			print("Leaving nama mata kuliah empty will update the value to empty as well.")

		print('Edit sks:')
		sks = input()

		if sks == "":
			print("Leaving sks empty will update the value to empty as well.")

		print('Edit semester:')
		semester = input()

		if semester == "":
			print("Leaving semester empty will update the value to empty as well.")

		cursor = self.__db.cursor()

		cursor.execute ("UPDATE "+self.__table_name+" SET namamtk=%s, sks=%s, semester=%s WHERE kodemtk=%s ", (namamtk, sks, semester, kodemtk))

		self.__db.commit()

		print(cursor.rowcount, "record update.")

	def delete(self):
		print('Search by kode mata kuliah to delete:')
		kodemtk = input()

		cursor = self.__db.cursor()

		cursor.execute ("DELETE FROM "+self.__table_name+" WHERE kodemtk = %s", (kodemtk,))

		self.__db.commit()

		print(cursor.rowcount, "record deleted.")

	def createConnection(self):
		db = mysql.connector.connect(
		  host     = self.__localhost,
		  user     = self.__username,
		  passwd   = self.__password,
		  database = self.__database_name
		)

		self.__db = db

