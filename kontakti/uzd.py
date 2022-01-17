import gramatina

def kontaktu_piev():
  vards= input('LUDZU IEVADIET KONTAKTA VARDU')
  numurs= input('ludzu ievadiet kontakta numuru')
  
  print(f'pievieno{vards}"ar numuru -{numurs}')

  gramatina.piev_kontaktu(vards, numurs)

kontaktu_piev()
#kontaktu atrašana

def kont_atrasana():
  vards=input('ludzu ievadi kontakta vardu kuru mekle')
  numurs= gramatina.atrod_kontaktu(vards)
  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    sakrit= gramatina.kont_meklesana(vards)
    if sakrit:
      for k in sakrit:
        print(f"{k}numurs ir {sakrit[k]}")
    print(f'izkatas, ka {vards} nav saraksta')

def kontaktu_red():
  iepr_v=input('ivadi vārdu kuru gribi rediģēt:')
  iepr_numurs = gramatina.atrod_kontaktu()

if iepr_numurs:
  jaunais_v=input(f"Ievadi {iepr_v} kontakta jauno vardu:")
  jaunais_n=input(f'ievadi {iepr_numurs} :')

if not jaunais_v:
  gramatina.mainit_numuru(iepr_v, jaunais_n)

if not jaunais_n:




def galvena_izvele():
 sakums = ("lmao")
 print(sakums)
 izvele=input('izveleta darbiba')

 if izvele =='1':
    kontaktu_piev()
 elif izvele =='2':
   kont_atrasana()
 else: 
    print('nav tādas, mēģini velreiz')

while True:
  galvena_izvele()
  input('\nNospiediet Enter, lai turpinātu\n\n')

