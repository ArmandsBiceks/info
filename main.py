klients = input('ievadi savu vardu un uzvardu:')
veltijums = input('raksti savu veltijumu:')
izmers = input('ladites izmeri:' )
materials = input('materiala cena:')

class Rekins:
  def __init__(self, klients, veltijums, izmers, materials):
    self.klients = klients
    self.veltijums = veltijums
    self.izmers = izmers
    self.materials = materials
    
    self.veltijuma_garums = len(self.veltijums)
    self.izmeru_sar = self.izmers.split(',')
    self.platums = self.izmeru_sar[0]
    self.garums = self.izmeru_sar[1]
    self.augstums = self.izmeru_sar[2]

  def izdrukat(self):
    print('\n\n')
    print('\033[1m'+'Pasūtija dati:'+'\033[0m')
    print('.'*50)
    print(f'\x1B[3mPārsūtija vārds un uzvārds:\x1B[0m \033[1;32mklients\033[1;0m')

    self.aprekins()

    self.saglabat()
    print()

  def aprekins(self):
    darba_samaksa = 15
    PVN = 21
    produkta_cena = (self.veltijuma_garums) * 1.2 + (self.platums/100 * self.garums/100 * self.augstums/100)/ 3 * self.materiala_cena
    PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
    rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
    
  
    return rekina_summa

  def saglabat():

    import csv

    with open (f'(self.klient).csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['klienta vārds','veltijums','izmēri','kokmateriala cena'])

a = Rekins(klients, izmers, veltijums, izmers)
a.izdrukat()


# print(izmers)

# print(type(izmers))
# print(izmers.split(','))
# sad=izmers.split(',')
# print(sad[0])



