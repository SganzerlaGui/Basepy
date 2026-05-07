import json

from dados import *

with open('inventario.json', 'r', encoding='utf-8') as f:
    invent = json.load(f)

info = {"usuario": "Guilherme","Idade": "18", "senha": "1234"}
invent.append(info)

cadastro()




print(invent)   