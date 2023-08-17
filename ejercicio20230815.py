class Paciente:
    def __init__(self, nombre, fecha_de_nacimiento, genero, fecha_ingreso, fecha_salida, enfermedad, diagnostico):
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.genero = genero
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.enfermedad = enfermedad
        self.diagnostico = diagnostico

    def actualizar_diagnostico(self):
        self.diagnostico =input("Ingrese nuevo diagnostico: ")
        return "El nuevo diagnostico es {}".format(self.diagnostico)
    
    def actualizar_fecha_salida(self):
        self.fecha_salida =input("Ingrese nueva fecha de salida: ")
        return "La nueva fecha de salida es {}".format(self.fecha_salida)
    
mi_paciente = Paciente("Nombre Beatriz Marín:", "Fecha de nacimiento 1964/11/13", "Genero Femenino:", "Fecha de ingreso 2023/08/17:", input("Ingrese la fecha de salida del paciente: "), "Tos", input("Ingrese el diagnostico del paciente: "))

print(mi_paciente.actualizar_diagnostico())
print(mi_paciente.actualizar_fecha_salida())
    