import json

with open("Data/clientes.json", "r") as archivo:
    clientes = json.load(archivo)

for cliente in clientes:
    print(cliente["nombre"])

