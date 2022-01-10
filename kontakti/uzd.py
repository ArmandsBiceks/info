import gramatina

def kontaktu_piev():
  vards= input('LUDZU IEVADIET KONTAKTA VARDU')
  numurs= input('ludzu ievadiet kontakta numuru')
  
  print(f'pievieno{vards}"ar numuru -{numurs}')

  gramatina.piev_kontaktu(vards, numurs)

kontaktu_piev()

def kont_atrasana():
  vards=input('ludzu ievadi kontakta vardu kuru mekle')
  numurs= gramatina.atrod_kontaktu(vards)
  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    print(f'izkatas, ka {vards} nav saraksta')