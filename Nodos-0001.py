class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.accion = None

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

class Jarvis:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, palabra, accion):
        self.nodos[palabra] = Nodo(palabra)
        self.nodos[palabra].accion = accion

    def ejecutar_accion(self, frase):
        palabras = frase.split()
        for palabra in palabras:
            if palabra in self.nodos:
                self.nodos[palabra].accion.ejecutar()
            else:
                print(f"No se encontró acción para la palabra '{palabra}'")

# Crear el árbol de decisión
jarvis = Jarvis()
jarvis.agregar_nodo("buscar", Buscar())
jarvis.agregar_nodo("imaginar", Imaginar())
jarvis.agregar_nodo("escribir", Escribir())

while True:
    frase = input("Ingrese una frase: ")
    jarvis.ejecutar_accion(frase.lower()) 
