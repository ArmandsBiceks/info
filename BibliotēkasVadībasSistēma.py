import sqlite3

class BblVald():
  def __init__(self, autors, nosaukums):
    self.autors=autors
    self.nosaukumi=nosaukums 
  
  def Marsuti(self):
    if self.autors=="A.Brigadere"and self.nosaukums=="Sprīdītis":
      self.cena=6

def Gr_cena(self):
  return f"Grāmatas {self.autors}-{self.nosaukums} cena ir {self.cena} EUR"

def Cena(self):
  return "Cena"

def Pakalpojuma_info(self):
  return f"Izvēlētā grāmata, autors un cena"

def Pakalpojuma_info_print(self):
  db=sqlite3.connect("dati.db")
  db.execute(
    """
   CREATE TABLE IF NOT EXISTS gramatas
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    autors TEXT,
    nosaukums TEXT,
    cena FLOAT,
    )
    """
    )
  db.execute("""
                INSERT INFO gramatas
                (autors, nosaukums, cena)
                VALUES(:autors, :nosaukums, :cena)
                 """,
    {"autors":self.autors,"nosaukums":self.nosaukums,"cena":self.cena})

  db.commit()

def Klients_info(self, vards, uzvards, per_kods, tel_nr):
  self.vards=vards
  self.uzvards=uzvards
  self.per_kods=per_kods
  self.tel_nr=tel_nr

  return f"Vārds{self.vards}, uzvards:{self.uzvards}, personas kods:{self.per_kods}, telefona numurs:{self.tel_nr}"

def Klients_info_print(self):
  db=sqlite3.connect("dati.db")
  db.execute(
  """
  CREATE TABLE IF NOT EXISTS klients
  (id INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
  vards TEXT,
  uzvards TEXT,
  per_kods TEXT,
  tel_nr INT
  )
  """
  )
  db.execute("""
              INSERT INTO klients
              (vards, uzvards, per_kods, tel_nr)
              VALUES(:vards,:uzvards, :per_kods, :tel_nr)
              """,
  {"vards":self.vards,"uzvards":self.uzvards,"per_kods":self.per_kods, "tel_nr":self.tel_nr})

  db.commit()
def datuIzvade(self):
  db=sqlite3.connect("dati.db")
  dati=db.execute("""
                 SELECT * FROM gramatas
                 JOIN klients
                 ON gramatas.id=klients.id
                 """)
  rezultāts=dati.fetchall()
  return rezultāts

import PySimpleGUI as sg

sg.theme("DarkAmber")
layout=[sg.Text("Bibliotēkas informācijas sistēma")],
[sg.Text("Autors:"), sg.InputText()],
[sg.Text("Nosaukums"), sg.InputText()],
[sg.Button("meklēt")]

layout2 = [[sg.Text("Izvēlētā grāmata:", key= "-GRAMATA-")],
[sg.Text("Vārds:"), sg.InputText()],
[sg.Text("Uzvārds:"), sg.InputText()],
[sg.Text("Personas kods:"), sg.InputText()],
[sg.Text("Telefona numurs:"), sg.InputText()],
[sg.Button("Pirkt")],
[sg.Text("Šeit būs personas dati", key='-DATI-')]]

layout3= [[sg.Text('Dati', key='-DATI-')]]

tabgrp = [
  [
    sg.TabGroup([[
    sg.Tab('Grāmata',layout),
    sg.Tab('Pirkt', layout2),
    sg.Tab('Dati', layout3)
  ]]),
sg.Button('Aizvērt')
  ]  
] 

window=sg.Window("InfSistema",tabgrp)
while True:
  event, values = window.read()
  if event =="Meklēt":
    autors=values[0]
    nosaukums=values[1]
    gramata=BblVald(autors, nosaukums)
    gramata.gramata()
    window['-CENA-'].update(gramata.cena)

    
  if event=="Pirkt":
    vards=values[2]
    uzvards=values[3]
    per_kods=values[4]
    tel_nr=values[5]

    window["-DATI-"].update(gramata.Klients_info(vards,uzvards,per_kods,tel_nr))
    
  gramata.Pakalpojuma_info_print()
  gramata.Klients_info_print()

  window["-DATUB-"].update(gramata.datuIzvade())

  if event in (sg.WIN_CLOSED, "Aizvērt"):
    break

window.close()