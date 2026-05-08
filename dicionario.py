import json

from dados import *

with open('inventario.json', 'r', encoding='utf-8') as f:
    invent = json.load(f)

    
info_recebida = cadastro()

invent.append(info_recebida)



print(invent)   