import pytest
from clases import Participante, Taller

def test_integracion_inscripcion():
    taller = Taller("Workshop Moda", 2)
    p1 = Participante("Ana", 20, "ana@mail.com")
    p2 = Participante("Luis", 21, "luis@mail.com")

    assert taller.inscribir_participante(p1) is True
    assert taller.inscribir_participante(p2) is True
    # Lista de inscritos se actualiza correctamente
    nombres = [p.nombre for p in taller.lista_inscritos]
    assert nombres == ["Ana", "Luis"]
    # No puede inscribir más participantes
    p3 = Participante("Marta", 22, "marta@mail.com")
    assert taller.inscribir_participante(p3) is False