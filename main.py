from Database import Database
from ZoologicoCLI import ZoologicoCLI


db = Database(database="S202-L2_EA1", collection="Animais")
db.resetDatabase()

zoologicoCLI = ZoologicoCLI(db)
zoologicoCLI.menu()
