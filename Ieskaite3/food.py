
from replit import db

def pievienot_edienu(ed, cena):
  if ed in db:
    print('Jau ir tāds')
  else:
    db[ed]=cena
    print(f'Pievienots:{ed}:${cena}')


def atrod_edienu(ed):
  cena = db.get(ed)
  return cena


def edienu_meklesana(simbols):

  meklet=db.prefix(simbols)
  return{k:db[k] for k in meklet}

  
def mainit_cenu(iepr_e,jauna_c):
  db[iepr_e]=jauna_c


def mainit_edienu(iepr_e, jaunais_e,jauna_c):
  db[jaunais_e]=jauna_c
  del db[iepr_e]


def dzest_edienu(ed):
  del db[ed]
  print(f'{ed} ir noņemts no ēdienkartes')  