
import tkinter as tk
window = tk.Tk()
lbl_sveiki = tk.Label (text = 'Sveika, Pasaule!')
lbl_sveiki.pack()


lbl_sveiki = tk.Label(
text = "Sveika, Pasaule!",
foreground="white", # Teksta krāsa - balta
background='black', # Fona krāsa - melna
)   


lbl_citads = tk.Label(
text = "Jāpamēģina!",
background="#34A2FE",
width=10, #Platums
height=5 #Augstums
)

btn_poga = tk.Button(
text="Noklikšķini!",
width=25,
height=5,
bg="blue", #saīsinājums background
fg="yellow", #saīsinājums foreground
)
btn_poga.pack()
lbl_sveiki.pack()
lbl_citads.pack()
lbl_sveiki.pack(fill=tk.X)
lbl_citads.pack(side=tk.LEFT)
def noklikskina(event):
  print("Noklik")
btn_poga.bind("<Button-1>", noklikskina)
#lodziņš 'jāpamēģina!' tika līdzināts pa kreisi
lbl_citads.pack(side=tk.RIGHT)

def noklikskina_lab(event):
  print("Bruhhh!")
btn_poga.bind("<Button-3>", noklikskina_lab)
window.mainloop()