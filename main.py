import random
import matplotlib.pyplot as plt
from Algoritmos import crear_pasajeros, generar_rango_cruza, generar_primer_p, arr_numeros, llenar_resultado
from Individuo import Individuo


class AlgoritmoGenetico:
    def __init__(self):
        # Variables que se pueden modificar
        n_pasajeros = 8
        self.n_mutaciones = 2
        self.n_individuos = 8
        self.n_generaciones = 10
        self.k = 3
        self.ancho_moto = 150
        self.id_indiv = 1
        self.cant_genes = arr_numeros(self.n_individuos)
        self.pasajeros = crear_pasajeros(n_pasajeros)
        self.poblacion = []
        self.nueva_poblacion=[]
        self.mejor_individuo=[]
        self.peor_individuo=[]
        self.primera_gen()

    def primera_gen(self):
        lista = generar_primer_p(self.pasajeros)
        for _ in range(self.n_individuos):
            random.shuffle(lista)
            self.crear_individuo(lista[:],False)
    def mutacion(self):
        # print("Poblacion iniciales: ", self.poblacion)
        for index, individuo in enumerate(self.nueva_poblacion):
            for _ in range(self.n_mutaciones):
                a, b = random.choices(self.cant_genes, k=2)
                individuo.data[a], individuo.data[b] = individuo.data[b], individuo.data[a]
        # print("Poblacion Mutada: ", self.poblacion)

    def cruza(self, indiv1, indiv2):
        # llenado parametros iniciales
        resultado = []
        indiv1_copy = indiv1.copy()
        index_aux = 0
        resultado = llenar_resultado(self.n_individuos)
        a, b = generar_rango_cruza(self.cant_genes)

        # se introduce a resultado los valores seleccionados del primer individuo
        for i in range(a, b+1):
            resultado[i] = indiv1[i]
            index_aux = i

        # for para eliminar los datos que ya se usaron del individuo1 (se creó un arreglo auxiliar)
        for i in range(a, b+1):
            indiv1_copy.remove(indiv1[i])

        datos_restantes = len(indiv1)-len(indiv1[a:b+1])
        index_aux += 1
        aux_result = index_aux
        aux_indv2 = index_aux
        for _ in range(datos_restantes):

            band = False
            while band == False:
                if aux_indv2 >= len(indiv2):
                    aux_indv2 = 0
                if aux_result >= len(resultado):
                    aux_result = 0
                if indiv2[aux_indv2] in indiv1_copy:
                    resultado[aux_result] = indiv2[aux_indv2]
                    indiv1_copy.remove(indiv2[aux_indv2])
                    aux_result += 1
                    aux_indv2 += 1
                    band = True
                else:
                    aux_indv2 += 1
        self.crear_individuo(resultado,True)
        
    def crear_individuo(self,data,is_nueva_poblacion):
        aptitud_del_indiv=self.calc_aptitud_de_indv(data)
        individuo=Individuo(self.id_indiv, data,aptitud_del_indiv[0],aptitud_del_indiv[1])
        self.poblacion.append(individuo)
        if is_nueva_poblacion==True:
            self.nueva_poblacion.append(individuo)
        self.id_indiv += 1
        for indiv in self.poblacion:
            indiv.set_pago(self.calcular_tarifa_a_pagar(indiv))
        for indiv in self.poblacion:
            indiv.set_aptitud(self.k)

    def encontrar_pasajero(self, id_pasajero):
        for pasajero in self.pasajeros:
            if pasajero.id == id_pasajero:
                return pasajero
        return None
    

    def calc_aptitud_de_indv(self, indiv):
        suma_cadera=0
        suma_costo=0
        num_pasajeros=0
        for gen in indiv:
            suma_cadera+=(self.encontrar_pasajero(gen).cadera)
            if suma_cadera<self.ancho_moto:
                suma_costo+=self.encontrar_pasajero(gen).aptitud
                num_pasajeros+=1
            else:
                break
        return [round(suma_costo,1),num_pasajeros]


    def calcular_tarifa_a_pagar(self, indiv):
        suma=0
        for i in range(indiv.pasajeros_arriba):
            suma+=self.encontrar_pasajero(indiv.data[i]).pago
        return suma
    def ordenar_poblacion(self):
        self.poblacion.sort(key=lambda x: x.aptitud, reverse=True)
    
       
    def poda(self):
        while len(self.poblacion)!=self.n_individuos:
            self.poblacion.pop()
    def ordenar_poblacion(self):
        self.poblacion.sort(key=lambda x: x.ganancia, reverse=True)

    def grafica1(self):
        list_aptitud = []
        list_epocas = []
        for i in range(self.n_generaciones):
            list_epocas.append(i+1)  
        for k in self.mejor_individuo:
            list_aptitud.append(k.ganancia)
        print(list_aptitud)    
        fig, ax = plt.subplots()
        ax.bar(list_epocas, list_aptitud)
        plt.show()    



# def print_grafica(algoritmo):


if __name__ == '__main__':
    algoritmo = AlgoritmoGenetico()
    # algoritmo.mutacion()
    print(f'Pasajeros')
    for pasajero in algoritmo.pasajeros:
        print(pasajero)
    
    
    algoritmo.ordenar_poblacion()
    print(f'Primera generacion: \n')
    for indv in algoritmo.poblacion:
        print(indv)
    

    x=0
    while x<algoritmo.n_generaciones:
        #Cruza 
        algoritmo.nueva_poblacion=[]
        for i in range(len(algoritmo.poblacion)):
            if i==len(algoritmo.poblacion):
                algoritmo.cruza(algoritmo.poblacion[i].data, algoritmo.poblacion[0].data)
            algoritmo.cruza(algoritmo.poblacion[i].data, algoritmo.poblacion[i+1].data)

        #Mutacion
        algoritmo.mutacion()
        algoritmo.ordenar_poblacion()

        algoritmo.poda()
        #algoritmo.mejor_ganancia()
        
        print(f'Población post cruza y mutacion generacion {x+1}')
        # print(f'Mejor individuo: {algoritmo.mejor_individuo}')
        algoritmo.mejor_individuo.append(algoritmo.poblacion[0])
        algoritmo.peor_individuo.append(algoritmo.poblacion[len(algoritmo.poblacion)-1])
        print(f'Mejor individuo: {algoritmo.poblacion[0]}')
        print(f'Peor individuo: {algoritmo.poblacion[len(algoritmo.poblacion)-1]}')
        for indv in algoritmo.poblacion:
            print(indv)
        x+=1
    algoritmo.grafica1()
    
