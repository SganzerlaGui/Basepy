import json

from dados import *

with open('inventario.json', 'r', encoding='utf-8') as f:
    invent = json.load(f)

    
cadastro()

invent.append(info)



print(invent)   