class Pasajero:
    def __init__(self,id,cadera,masa,pago):
        self.id=id
        self.cadera=cadera
        self.masa=masa
        self.pago=pago
        self.calc_aptitud()
    def calc_aptitud(self):
        costo_por_kg=0.04
        self.aptitud=round(self.masa*costo_por_kg,1)

    def __repr__(self):
        return str(self.__dict__)
    
