import tkinter as tk
window = tk.Tk()


from PIL import Image

def bilde():

  datne = 'homeless.jpg'

  with Image.open(datne) as im:

    print(datne, im.format, f'{im.size}x{im.mode}')
    im.show()

    izmers = (100,100)

    im.thumbnail(izmers)

    im.save('Apelsino.jpg', im.format)


bilde()