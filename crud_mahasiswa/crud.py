import mysql.connector

class CRUD:

	def __init__(self):
		self.__localhost     = "localhost"
		self.__username      = "root"
		self.__password      = ""
		self.__database_name = "python_crud_kuliah"
		self.__table_name 	 = "mahasiswa"
		self.createConnection()

	def create(self):
		print('Enter your nim: ')
		nim = input()
		print('Enter your name: ')
		name = input()

		cursor = self.__db.cursor()

		val = (nim, name)
		cursor.execute("INSERT INTO "+self.__table_name+" (nim, name) VALUES (%s, %s)", val)

		self.__db.commit()

		print(cursor.rowcount, "record inserted.")

	def read(self):
		cursor = self.__db.cursor()

		cursor.execute("SELECT * FROM "+self.__table_name+"")

		myresult = cursor.fetchall()
		for x in myresult:
		  print(x)

	def update(self):
		print('Search by nim:')
		nim = input()

		print('Edit name:')
		name = input()

		if name == "":
			print("Leaving name empty will update the value to empty as well.")

		cursor = self.__db.cursor()

		cursor.execute ("UPDATE "+self.__table_name+" SET name=%s WHERE nim=%s ", (name, nim))

		self.__db.commit()

		print(cursor.rowcount, "record update.")

	def delete(self):
		print('Search by nim to delete:')
		nim = input()

		cursor = self.__db.cursor()

		cursor.execute ("DELETE FROM "+self.__table_name+" WHERE nim = %s", (nim,))

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

