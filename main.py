klients = input('ievadi savu vardu un uzvardu:')
veltijums = input('raksti savu veltijumu:')
izmers = input('ladites izmeri:' )
materials = input('materiala cena:')

class Rekins:
  def _init_(self, klients, veltijums, izmers, materials):
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
  pass

def aprekins(self):
 darba_samaksa = 15
 PVN = 21
 produkta_cena = (veltījuma teksta garums simbolos) * 1.2 +
 (platums/100 * garums/100 * augstums/100)/ 3 * materiala_cena
 PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
 rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

a = rekins(klients, izmers, veltijums, izmers)


print(izmers)

print(type(izmers))
print(izmers.split(','))
sad=izmers.split(',')
print(sad[0])