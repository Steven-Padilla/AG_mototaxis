class Individuo :
    def __init__(self,id,data,suma_costo_pasajero,pasajeros_arriba):
        self.id =id
        self.data =data
        self.suma_costo_pasajeros=suma_costo_pasajero 
        self.pasajeros_arriba=pasajeros_arriba
    def set_pago(self,pago):
        self.pago=pago
    def set_aptitud(self,k):
        aptitud=self.pago-(k+self.suma_costo_pasajeros)
        self.ganancia=round(aptitud,1)
    def __repr__(self):
        return str(self.__dict__)
    
