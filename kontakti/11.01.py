from replit import db

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



