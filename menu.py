class Menu:
    def __init__(self, nm, opc):
        self.nombreMenu= nm
        self.opciones= opc

    
    def menus(self):
        print(self.nombreMenu)
        for opcion in self.opciones:
            print(opcion)
        opc=int(input("Elija la opción del 1 al {} que desea escoger: ".format(len(self.opciones))))
        while   opc < 1 or  opc > len(self.opciones) :
            opc=int(input("Ingrese una opcion que sea valida: "))
        return opc
