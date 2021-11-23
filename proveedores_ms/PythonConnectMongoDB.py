#mongodb => AtlasLink
#Instalar el environment
#Instalar Pymongo:
#python -m pip install pymongo=3.7.2
#pip install pymongo[srv]

import pymongo
from pymongo import MongoClient

cliente = pymongo.MongoClient("enlace de Atlas para conectar con el Baas")
db = cliente.misionticdb
datos = db.usuarios.find()
for dato in datos:
    print(dato["clave"])
    print(dato)