class Participante:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def es_mayor_edad(self):
        return self.edad >= 18


class Taller:
    def __init__(self, nombre, limite_asistentes):
        self.nombre = nombre
        self.limite_asistentes = limite_asistentes
        self.lista_inscritos = []

    def cupos_disponibles(self):
        return self.limite_asistentes - len(self.lista_inscritos)

    def inscribir_participante(self, participante):
        if participante.es_mayor_edad() and self.cupos_disponibles() > 0:
            self.lista_inscritos.append(participante)
            return True
        return False

class SistemaReservas:
    def __init__(self):
        self.talleres = []

    def agregar_taller(self, taller):
        self.talleres.append(taller)

    def procesar_pago(self, participante, monto):
        """
        Simula el procesamiento de un pago.
        Devuelve True si el pago es exitoso, False si falla.
        Simulación: el pago falla si el monto es negativo o el participante no tiene email válido.
        """
        if monto <= 0:
            return False
        if not participante.email or '@' not in participante.email:
            return False
        # Simulación: 90% de probabilidad de éxito (por defecto exitoso)
        return True

    def registrar_participante_en_taller(self, participante, taller, monto=0):
        """
        Registra un participante en un taller solo si el pago es procesado exitosamente.
        """
        if taller not in self.talleres:
            return False
        
        # Procesar pago
        if not self.procesar_pago(participante, monto):
            return False
        
        # Si el pago fue exitoso, inscribir en el taller
        return taller.inscribir_participante(participante)

    def listar_participantes_taller(self, taller):
        return [p.nombre for p in taller.lista_inscritos]
    
class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def asignar_taller(self, taller):
        taller.profesor = self
    
    def obtener_talleres_asignados(self, sistema_reservas):
        return [t for t in sistema_reservas.talleres if hasattr(t, 'profesor') and t.profesor == self]