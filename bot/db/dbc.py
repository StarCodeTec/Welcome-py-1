import sys
sys.path.append("..")
import passcodes
password=passcodes.main.dbc
client = f"mongodb+srv://Jagg312:{password}@pybot00.74vkk.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NON?ssl=true"
