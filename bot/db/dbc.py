from .. import passcodes
password=passcodes.main.dbc
client = pymongo.MongoClient(f"mongodb+srv://Jagg312:{password}@pybot00.74vkk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
