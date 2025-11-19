from Figurasgeometricas import Figurasgeometricas


class Pentagono(Figurasgeometricas):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    @property
    def perimetro(self) -> float:
       return self._perimetro
    
    @perimetro.setter
    def perimetro(self, perimetro: float):
        self._perimetro = perimetro     

    @property
    def apotema(self) -> float:
        return self._apotema
    
    @apotema.setter
    def apotema(self) -> float:
        return self._apotema

    @apotema.setter
    def apotema(self,apotema:float):
        self._apotema = apotema
    

        
    def area(self):
        return self.perimetro * self.apotema / 2 