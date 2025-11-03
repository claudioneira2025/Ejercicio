import math


class Circulo:
    def __init__(self,radio:int):
        self.radio=radio

    def area(self):
        return math.pi*math.pow(self.radio,2)
    
  
        