import sqlite3

db=sqlite3.connect('test.db')

#tabula

db.execute("""
          CREATE TABLE IF NOT EXISTS darbinieki
           (id    INTEGER  PRIMARY KEY  NOT NULL,
           vards   TEXT  NOT NULL,
           alga    REAL,
           piezimes  CHAR(50)
           )
           """)

db.execute(""" INSERT INTO darbinieki
           (id,vards,alga,piezimes)
           VALUES(1,"Anna",980.50,"Ekonomiskas")
           """)

db.commit()

datu iegušana
dati=db.execute("""SELECT*FROM darbinieki
                WHERE id=]
               """)
rezultats=dati.fetcha
print(rezultats)
#tabulas izveide izmantojot id generesanu
db.execute(
"""
CREATE TABLE IF NOT EXISTING
(id  INTEGER  PRIMARY KEY  AUTOINCREMENT  NOT NULL,
pceturksnis REAL,
oceturksnis REAL,
tceturksnis REAL,
cceturksnis REAL
)
"""
)
p_ceturksnis=Input('Ievadi pirmā ceturksņa prēmiju')
o_ceturksnis=Input('Ievadi otrā ceturksņa prēmiju')
t_ceturksnis=Input('Ievadi trešā ceturksņa prēmiju')
c_ceturksnis=Input('Ievadi ceturtā ceturksņa prēmiju')
db.execute(
"""
INSERT INTO premijas
(pceturksnis, oceturksnis, tceturksnis, cceturksnis)
VALUES[:'pceturksnis,':'p_ceturksnis','oceturksnis':o_ceturksnis,'tceturksnis':t_ceturknis,'cceturksnis':c_ceturksnis ]
"""
)
  db.commit()
dati =db.execute("""SELECT*FROM premijas
                 WHERE id