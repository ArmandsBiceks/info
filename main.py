import d_gramatina

from replit import db

def piev_kontaktu(vards, tel_nr):
  if vards in db:
    print('Kontakts jau ir pievienots')
  else:
    db[vards]=tel_nr
    print(f'Pievienots:{vards}:{tel_nr}')



sg.TabGroup('Spēlētāju dati, layout2')]])

  sg.Button('Aizvērt')]

layout2=[[sg.text('spēlētāju dati')]]

tabgrp=[
  [
    sg.TabGroup[
      sg.Tab('spēle, layout')