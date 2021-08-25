class Pila:
    def __init__(self,tamaño):
        self.__lista=[]
        self.__tope=0
        self.size=tamaño

    def empty(self):
        return self.__tope==0

    def push(self,dato):
        if self.__tope < self.size:
            self.__lista+= [dato]
            self.__tope+= 1
            print("El valor {} ha sido ingreado".format(dato))
        else: print("ERROR DE INGRESO: La lista está llena")
    
    def pop(self):
        if self.empty(): return -1
        else:
            top= self.__lista[-1]
            self.__tope-= 1
            self.__lista= self.__lista[:-1]
            return top

    def show(self):
        if self.empty(): print("No hay valores para mostrar")
        else:
            for top in range(self.__tope-1,-1,-1):
                print("[{}]".format(self.__lista[top]))
        
    def longitud(self):
        return self.__tope
