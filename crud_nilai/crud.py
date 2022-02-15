import mysql.connector

class CRUD:

	def __init__(self):
		self.__localhost     = "localhost"
		self.__username      = "root"
		self.__password      = ""
		self.__database_name = "python_crud_kuliah"
		self.__table_name 	 = "nilai"
		self.createConnection()

	def create(self):
		print('Input nim: ')
		nim = input()
		print('Input kode mata kuliah: ')
		kodemtk = input()
		print('Input nilai akhir: ')
		na = input()

		cursor = self.__db.cursor()

		val = (nim, kodemtk, na)
		cursor.execute("INSERT INTO "+self.__table_name+" (nim, kodemtk, na) VALUES (%s, %s, %s)", val)

		self.__db.commit()

		print(cursor.rowcount, "record inserted.")

	def read(self):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+"")

		myresult = cursor.fetchall()

		for x in myresult:
		  print(x)

	def update(self):
		print('Search by nim :')
		nim = input()
		print('Search by kode mata kuliah :')
		kodemtk= input()

		print('Edit nilai akhir:')
		na = input()

		if na == "":
			print("Leaving nilai akhir empty will update the value to empty as well.")


		cursor = self.__db.cursor()

		cursor.execute ("UPDATE "+self.__table_name+" SET na=%s WHERE nim=%s && kodemtk=%s ", (na, nim, kodemtk))

		self.__db.commit()

		print(cursor.rowcount, "record update.")

	def delete(self):
		print('Search by nim to delete:')
		nim = input()
		print('Search by kode mata kuliah to delete:')
		kodemtk = input()

		cursor = self.__db.cursor()

		cursor.execute ("DELETE FROM "+self.__table_name+" WHERE nim=%s && kodemtk=%s", (nim,kodemtk))

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

