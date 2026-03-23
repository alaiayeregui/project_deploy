import pytest
from clases import Participante, Taller, SistemaReservas

def test_flujo_completo():
    sistema = SistemaReservas()
    
    taller1 = Taller("Desfile Primavera", 2)
    taller2 = Taller("Workshop Otoño", 1)
    
    sistema.agregar_taller(taller1)
    sistema.agregar_taller(taller2)
    
    p1 = Participante("Ana", 20, "ana@mail.com")
    p2 = Participante("Luis", 17, "luis@mail.com")  # menor de edad
    p3 = Participante("Marta", 25, "marta@mail.com")
    
    # Inscribir participantes en varios talleres
    assert sistema.registrar_participante_en_taller(p1, taller1) is True
    assert sistema.registrar_participante_en_taller(p2, taller1) is False  # menor
    assert sistema.registrar_participante_en_taller(p3, taller2) is True

    # Listado final de participantes
    assert sistema.listar_participantes_taller(taller1) == ["Ana"]
    assert sistema.listar_participantes_taller(taller2) == ["Marta"]