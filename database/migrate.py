import database as db

db = db.Database("python_crud_kuliah")
db.setLocalhost("localhost")
db.setUsername("root")
db.setPassword("")
db.createDatabase()

db.setTableMahasiswa("mahasiswa")
db.setTableMk("matakuliah")
db.setNilai("nilai")
db.createTable()

