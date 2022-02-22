import json

vārdnīca={'Vards':'Janis', 'Izglitiba':'Videja','Vecums':20}


a=json.dumps(vārdnīca)

print(a)

print(json.dumps(['kivi','citrons']))


py_data{"Name":"Anna","Age":"30","Animals":True,"Kids":('Sinda','Aldis'),"Cars":[{"Model":'Audi','Year':2007]},{"Model":"BMW",'Year':2009]}

print(json.dumps(py_data,indent-2))

with open('json_dati','w',encoding="utf-8") as f:
json.dati=json.load(f)
print(len(json.dati))
print(json_dati.keys())
print(json_dati.values())

mekl_atslega="1"
ista atslega=" "
for atslega in json_dati.keys():
  if atslega==mekl_atslega:
    ista_atslega=atslega
    print(json_dati[atslega])
    if ista atslega!=mekl_atslega:
   print(json_dati[atslega])
else:
print(f'Izskatas,ka {mekl_atslega} nav sarakstā')

#funkcijas argumenti - datns nosaukums
#atvert failu

def json_las(datnesNosaukums,atslega):
  with open('datnesNosaukums',"r",encoding="utf-8") as f:
   json_dati=json.load(f)

  for atsl==