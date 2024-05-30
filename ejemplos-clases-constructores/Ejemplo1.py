class Persona:
    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"

# Crear un objeto de la clase Persona
persona1 = Persona()

# Establecer los atributos del objeto usando métodos
persona1.establecer_nombre("Juan")
persona1.establecer_edad(30)

# Obtener y usar los atributos del objeto usando métodos
print(persona1.saludar())  # Salida: Hola, mi nombre es Juan.
print(f"{persona1.obtener_nombre()} tiene {persona1.obtener_edad()} años.")  # Salida: Juan tiene 30 años.
