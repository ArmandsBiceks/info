

from replit import db

def piev_kontaktu(vards, tel_nr):
  if vards in db:
    print('Kontakts jau ir pievienots')
  else:
    db[vards]=tel_nr
    print(f'Pievienots:{vards}:{tel_nr}')

#meklet pēc pilna vārda

def atrod_kontaktu(vards):
  numurs = db.get(vards)
  return numurs

#meklet pec simbola

def kont_meklesana(simbols):

  meklet=db.prefix(simbols)
  return{k:db[k] for k in meklet}

#redig
def mainit_numuru(iepr_v,jaunais_n):
  db[iepr_v]=jaunais_n
#maina kont
def mainit_kontaktu(iepr_v, jaunais_v,jaunais_n):
  db[jaunais_v]=jaunais_n
  del db[iepr_v]
  print(f'KOntakta{iepr_v}jaunais vards ir{jaunais_v}')
#dzesana
def dzest_kont(vards):
  del db[vards]
  print(f'kontakts{vards} ir izdzēsts')  