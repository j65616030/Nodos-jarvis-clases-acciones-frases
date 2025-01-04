class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.accion = None
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        pass

class Buscar(Accion):
    def __init__(self):
        super().__init__("Buscar")

    def ejecutar(self):
        print("Buscando...")

class Imaginar(Accion):
    def __init__(self):
        super().__init__("Imaginar")

    def ejecutar(self):
        print("Imaginando...")

class Escribir(Accion):
    def __init__(self):
        super().__init__("Escribir")

    def ejecutar(self):
        print("Escribiendo...")

class MoE(Nodo):
    def __init__(self, palabra):
        super().__init__(palabra)

    def ejecutar_accion(self, frase):
        palabras = frase.split()
        for palabra in palabras:
            for hijo in self.hijos:
                if hijo.palabra == palabra:
                    hijo.accion.ejecutar()
                    break
            else:
                print(f"No se encontró acción para la palabra '{palabra}'")

# Crear el MoE
moe = MoE("moe")

# Agregar expertos al MoE
moe.agregar_hijo(Nodo("buscar"))
moe.hijos[0].accion = Buscar()
moe.agregar_hijo(Nodo("imaginar"))
moe.hijos[1].accion = Imaginar()
moe.agregar_hijo(Nodo("escribir"))
moe.hijos[2].accion = Escribir()

while True:
    frase = input("Ingrese una frase: ")
    moe.ejecutar_accion(frase.lower()) 
