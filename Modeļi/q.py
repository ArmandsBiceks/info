'''oop'''

saraksts = [1,2,3]

print(type(saraksts))

#class
#self
#_str_

class piem:  #Klases definē ar lielo burtu
  pass
a = piem()

print(type(a))

class car:
  def _init_(self, model):
    self.model=model

ford = car(model='focus')

opel = car(model='astra')

print(ford.model)