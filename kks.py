from PIL import image

def bilde():

  datne = 'kks/homeless.jpg'

  with image.open(datne) as im:

    print(datne, im.format, f'{im.size}x{im.mode}')
    im.show()


bilde()