class ListaFrutas:
    def __init__(self):
        self.frutas = []

    def agregar_fruta(self, fruta):
        self.frutas.append(fruta)

    def eliminar_fruta(self, fruta):
        self.frutas.remove(fruta)

    def ordenar_frutas(self):
        self.frutas.sort()

    def imprimir_frutas(self):
        print(self.frutas)

# Crear una instancia de la clase ListaFrutas
lista_frutas = ListaFrutas()

# Agregar frutas
lista_frutas.agregar_fruta('manzana')
lista_frutas.agregar_fruta('plátano')
lista_frutas.agregar_fruta('cereza')

# Agregar más frutas
lista_frutas.agregar_fruta('naranja')
lista_frutas.agregar_fruta('mango')

# Eliminar una fruta
lista_frutas.eliminar_fruta('cereza')

# Ordenar y mostrar las frutas
lista_frutas.ordenar_frutas()
lista_frutas.imprimir_frutas()
