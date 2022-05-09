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
              """)