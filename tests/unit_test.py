import pytest
from clases import Participante, Taller, SistemaReservas

def test_es_mayor_edad():
    p1 = Participante("Ana", 20, "ana@mail.com")
    p2 = Participante("Luis", 16, "luis@mail.com")
    assert p1.es_mayor_edad() is True
    assert p2.es_mayor_edad() is False

# Tests para el sistema de pagos
def test_procesar_pago_exitoso():
    """Verifica que el pago sea exitoso con datos válidos"""
    sistema = SistemaReservas()
    participante = Participante("Ana", 25, "ana@mail.com")
    assert sistema.procesar_pago(participante, 100) is True

def test_procesar_pago_falla_monto_negativo():
    """Verifica que el pago falle si el monto es negativo"""
    sistema = SistemaReservas()
    participante = Participante("Ana", 25, "ana@mail.com")
    assert sistema.procesar_pago(participante, -50) is False

def test_procesar_pago_falla_email_invalido():
    """Verifica que el pago falle si el email no es válido"""
    sistema = SistemaReservas()
    participante = Participante("Ana", 25, "ana_invalid")
    assert sistema.procesar_pago(participante, 100) is False

def test_registrar_participante_pago_exitoso():
    """Verifica que se registre correctamente si el pago es exitoso"""
    sistema = SistemaReservas()
    taller = Taller("Python Avanzado", 20)
    sistema.agregar_taller(taller)
    
    participante = Participante("Ana", 25, "ana@mail.com")
    resultado = sistema.registrar_participante_en_taller(participante, taller, monto=50)
    
    assert resultado is True
    assert "Ana" in sistema.listar_participantes_taller(taller)

def test_registrar_participante_pago_falla():
    """Verifica que NO se registre si el pago falla"""
    sistema = SistemaReservas()
    taller = Taller("Python Avanzado", 20)
    sistema.agregar_taller(taller)
    
    participante = Participante("Luis", 25, "luis_invalid")
    resultado = sistema.registrar_participante_en_taller(participante, taller, monto=50)
    
    assert resultado is False
    assert "Luis" not in sistema.listar_participantes_taller(taller)

def test_registrar_participante_sin_pago_monto_negativo():
    """Verifica que no se registre si el monto es negativo"""
    sistema = SistemaReservas()
    taller = Taller("Python Avanzado", 20)
    sistema.agregar_taller(taller)
    
    participante = Participante("Carlos", 30, "carlos@mail.com")
    resultado = sistema.registrar_participante_en_taller(participante, taller, monto=-100)
    
    assert resultado is False
    assert "Carlos" not in sistema.listar_participantes_taller(taller)

# cupos disponibles

# inscripciones
