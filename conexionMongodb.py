import pymongo

MONGO_HOST= "127.0.0.1"
MONGO_PUERTO= "27017"
MONGO_TIEMPO_FUERA= 1000

MONGO_URL="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS= "connection_ssh"
MONGO_COLECCION= "routes"

try:
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]
    direcciones_ip= []
    for datos in coleccion.find():
        direcciones_ip.append(datos["ip"])

    print(direcciones_ip)
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errortiempo:
    print("Tiempo excedido "+errortiempo)
except pymongo.errors.ConnectionFailure as errorconexion:
    print("Fallo al conectarse a Mongodb "+errorconexion)