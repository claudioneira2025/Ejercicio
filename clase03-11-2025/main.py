from clases.circulo import Circulo
from clases.cuentaBancaria import CuentaBancaria



CuentaBancaria=CuentaBancaria("123456","claudio neira",25000)
print (CuentaBancaria.mostrar_datos())

CuentaBancaria.depositar(1000000)
print (CuentaBancaria.mostrar_datos())
# circulo=Circulo(5)

# print(f"El Area del circulo es {round(circulo.area(),2)}")



#class Circulo:
#   def __init__(self,radio):
#      self.radio=radio
#
#   def area(self):
#      return math.pi*math.pow(self.radio,2)
