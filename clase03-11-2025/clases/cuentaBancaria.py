class CuentaBancaria:
    def __init__(self,numeroCuenta,titular,saldo):
        self.numeroCuenta=numeroCuenta
        self.titular=titular
        self.saldo=saldo
    
    def depositar(self,monto):
        self.saldo+=monto

    def retirar(self,monto):
         if self.saldo<monto:
             raise Exception("saldo insuficiente")
             self.saldo-=monto

    def mostrar_datos(self):
        return f"Cuenta {self.numeroCuenta} -Titular {self.titular}- saldo{self.saldo}"

#comontar seleccionar control kc
#  def retirar(self,monto):
#         if selt.saldo>=monto:
#             self.saldo-=monto
#         else:
#              print("La pobrezame esta respirando en la nuca")
