class Lista:
    def __init__(self,tamanio):
        self.lista = []
        self.longitud=0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            print("El valor {} ha sido ingresado correctamente".format(dato))
        else:
            print("ERROR DE INGRESO: La lista esta llena")
    
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return -1
        else:
            valor = self.lista[pos]
            listaAux= self.lista[0:pos]
            for indice in range (pos,self.longitud-1):
                listaAux+= [self.lista[indice+1]]
            self.longitud -= 1
            self.lista= listaAux
            return valor 
            
    def buscar(self,dato):
        ban = False
        for a in range(0,self.longitud):
            if dato == self.lista[a]:
                ban = True
                break
        if ban: return a
        else: return -1
            
    def insertar(self,dato):
        if self.buscar(dato) == -1:
            self.append(dato)
        else: return -1
                     
    def eliminar(self,dato):
        pos = self.buscar(dato)
        if pos != -1:
            self.obtener(pos)
            #self.lista = self.lista[0:pos] + self.lista[pos+1:]
            #self.longitud -= 1
        else: return -1                 
            
    def mostrar(self,orden):
        if orden == 1:
            for pos in range(0,self.longitud):
                print("[{}]".format(self.lista[pos]))
        else:
            for pos in range(self.longitud-1,-1,-1):
                print("[{}]".format(self.lista[pos]))
    
              
                     
