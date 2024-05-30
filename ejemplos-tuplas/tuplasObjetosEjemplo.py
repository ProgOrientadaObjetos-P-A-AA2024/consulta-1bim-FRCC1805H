class TuplaColores:
    def __init__(self, colores):
        self.colores = colores

    def obtener_color_por_indice(self, indice):
        return self.colores[indice]

    def desempaquetar(self):
        return self.colores

# Crear una instancia de la clase TuplaColores
tupla_colores = TuplaColores('rojo', 'verde', 'azul')

# Acceder a elementos por índice
primer_color = tupla_colores.obtener_color_por_indice(0)

# Desempaquetar la tupla
rojo, verde, azul = tupla_colores.desempaquetar()

# Imprimir los valores desempaquetados
print(rojo, verde, azul)
