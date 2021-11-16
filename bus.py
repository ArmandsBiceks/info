class transportlidzeklis:

  krasa='melna'

  def _init_(self, nosaukums, max_atrums, nobraukums):
   self.nosaukums = nosaukums
   self.max_atrums = max_atrums
   self.nobraukums = nobraukums

def sed_vietu_skaits(self, skaits):
  self.skaits = skaits
  return f'sedvietu skaits {self.nosaukums} ir {self.skaits}.'

def biletes(self):
  return self.skaits * 0.5

modelisX = transportlidzeklis('mersedess', 180, 2000,)
print(modelisX)

class buss(transportlidzeklis):
  def sedvietu_skaits(self,skaits=50):
    return super().sedviietu_skaits(skaits)

    def biletes(self):
      return super().biletes()

modelisX = buss('audi', 240, 1800)
print(modelisX.sedvietu_skaits, modelisX.)