import pySimpleGUI as sg

masivs=[(1,"Anna",15),(2,"Vilhelmine",36),(3,"Pēteris",40)]
print(len(masivs[0]))

layout=[]

for i in range(len(masivs)):
  layout=[sg.Text(f'{masivs[1][0]}'),sg.Text(f'{masivs[i][1]}'),sg.Text(f'{masivs[i][2]}')]
  layout=[[sg.Button('Save'),sg.Button('Exit')]]
window=sg.Window('Saraksts',layout)
event,values=window.read()