class Perro:
    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def ladrar(self):
        return f"{self.nombre} está ladrando."


# Crear un objeto de la clase Perro
mi_perro = Perro()

# Establecer los atributos del objeto usando métodos
mi_perro.establecer_nombre("Fido")
mi_perro.establecer_edad(3)

# Obtener y usar los atributos del objeto usando métodos
print(mi_perro.ladrar())            # Salida: Fido está ladrando.
print(f"{mi_perro.obtener_nombre()} tiene {mi_perro.obtener_edad()} años.")  # Salida: Fido tiene 3 años.
