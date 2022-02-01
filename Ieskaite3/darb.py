import food


def pievienot_edienu():
  ed= input('Ievadiet jaunā ēdiena nosaukumu:')
  cena= input('Ievadiet jaunā ēdiena cenu:')
  
  print(f'pievieno:{ed}-${cena}')

  food.pievienot_edienu(ed, cena)

pievienot_edienu()


def ediena_atrasana():
  ed=input('ludzu ievadi ēdiena nosaukumu kuru meklē:')
  cena= food.atrod_edienu(ed)
  if cena:
    print(f"{ed} cena ir {cena}")
  else:
    sakrit= food.ediena_meklesana(ed)
    if sakrit:
      for k in sakrit:
        print(f"{k}cena ir {sakrit[k]}")
    print(f'izkatas, ka {ed} nav saraksta')


def edienu_red():
  iepr_e = input('ivadi ēdienu kuru gribi rediģēt:')
  iepr_cena = food.atrod_edienu(iepr_e)

  if iepr_cena:
    jaunais_e=input(f"Ievadi {iepr_e} aizvietojumu:").strip()
    jauna_cena=input(f'ievadi {iepr_cena} jaunu cenu :')

    if not jaunais_e:
      jauna_cena=iepr_cena

    if not jaunais_e:
      food.mainit_cenu(iepr_e, jauna_cena)


    else:
      food.mainit_edienu(iepr_e, jaunais_e, jauna_cena)
  
  else:
    print(f'izskatas, ka {iepr_e} nav ēdienkartē')


def edienu_dzesana():
  ed=input('Ievadi edienu, kuru vēlies dzēst:')
  cena=food.atrod_edienu(ed)

  if cena:
    lemums=input(f'vai jus tiesam velaties dzest {ed}-{cena}?(1-jā, 2-nē)')
    if lemums =='1':
      food.dzest_edienu(ed)
    else:
      print(f'{ed} netika dzēsts')


def darbību_izvele():
 sakums = ("ēdienkarte")
 print(sakums)
 izvele=input('izveleta darbiba')

 if izvele =='1':
   pievienot_edienu()
 elif izvele =='2':
   ediena_atrasana()
 elif izvele=='3':
   edienu_red()
 elif izvele =='4':
   edienu_dzesana()
 else: 
    print('nav tādas, mēģini velreiz')

while True:
  darbību_izvele()
  input('\nNospiediet Enter, lai turpinātu\n\n')