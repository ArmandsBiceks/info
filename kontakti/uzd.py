import gramatina

def kontaktu_piev():
  vards= input('LUDZU IEVADIET KONTAKTA VARDU:')
  numurs= input('ludzu ievadiet kontakta numuru:')
  
  print(f'pievieno-{vards}"ar numuru-{numurs}')

  gramatina.piev_kontaktu(vards, numurs)

kontaktu_piev()
#kontaktu atrašana

def kont_atrasana():
  vards=input('ludzu ievadi kontakta vardu kuru meklē:')
  numurs= gramatina.atrod_kontaktu(vards)
  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    sakrit= gramatina.kont_meklesana(vards)
    if sakrit:
      for k in sakrit:
        print(f"{k}numurs ir {sakrit[k]}")
    print(f'izkatas, ka {vards} nav saraksta')
    
#redigesana

def kontaktu_red():
  iepr_v = input('ivadi vārdu kuru gribi rediģēt:')
  iepr_numurs = gramatina.atrod_kontaktu(iepr_v)

  if iepr_numurs:
    jaunais_v=input(f"Ievadi {iepr_v} kontakta jauno vardu:").strip()
    jaunais_n=input(f'ievadi {iepr_numurs} jaunu num :')

    if not jaunais_n:
      jaunais_n=iepr_numurs

    if not jaunais_v:
      gramatina.mainit_numuru(iepr_v, jaunais_n)


    else:
      gramatina.mainit_kontaktu(iepr_v, jaunais_v, jaunais_n)
  
  else:
    print(f'izskatas, ka {iepr_v} nav sarakstā')
#dzesana
def kont_dzesana():
  vards=input('Ievadi kontakta vardu, kuru vēlies dzēst:')
  numurs=gramatina.atrod_kontaktu(vards)

  if numurs:
    lemums=input(f'vai jus tiesam velaties dzest kont {vards}-{numurs}?(1-ja, 2-ne)')
    if lemums =='1':
      gramatina.dzest_kont(vards)
    else:
      print(f'kontakts {vards} netika dzēsts')



def galvena_izvele():
 sakums = ("lmao")
 print(sakums)
 izvele=input('izveleta darbiba')

 if izvele =='1':
    kontaktu_piev()
 elif izvele =='2':
   kont_atrasana()
 elif izvele=='3':
   kontaktu_red()
 elif izvele =='4':
   kont_dzesana()
 else: 
    print('nav tādas, mēģini velreiz')

while True:
  galvena_izvele()
  input('\nNospiediet Enter, lai turpinātu\n\n')

