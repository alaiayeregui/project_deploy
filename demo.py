from clases import Participante, Taller, SistemaReservas

def main():
    print("=== DEMO DEL SISTEMA DE RESERVAS DE TALLERES DE MODA ===\n")

    # Crear participantes
    p1 = Participante("Ana", 20, "ana@mail.com")
    p2 = Participante("Luis", 16, "luis@mail.com")
    p3 = Participante("Marta", 25, "marta@mail.com")

    print(f"Participantes creados: {p1.nombre}, {p2.nombre}, {p3.nombre}\n")

    # Crear talleres
    taller1 = Taller("Desfile Primavera", 2)
    taller2 = Taller("Workshop Otoño", 1)

    # Crear sistema y agregar talleres
    sistema = SistemaReservas()
    sistema.agregar_taller(taller1)
    sistema.agregar_taller(taller2)

    print(f"Talleres disponibles: {taller1.nombre} ({taller1.limite_asistentes} cupos), "
          f"{taller2.nombre} ({taller2.limite_asistentes} cupos)\n")

    # Inscribir participantes a través del sistema
    print("Inscribiendo participantes en taller1 mediante SistemaReservas:")
    for participante in [p1, p2, p3]:
        resultado = sistema.registrar_participante_en_taller(participante, taller1)
        print(f"- {participante.nombre}: {resultado}")

    print(f"\nCupos restantes en {taller1.nombre}: {taller1.cupos_disponibles()}\n")

    # Registrar un participante en taller2
    print("Registrando participante en taller2 mediante SistemaReservas:")
    resultado = sistema.registrar_participante_en_taller(p3, taller2)
    print(f"- {p3.nombre} inscrito en {taller2.nombre}? {resultado}\n")

    # Listado final de participantes
    print("=== LISTADO FINAL DE PARTICIPANTES POR TALLER ===")
    for taller in [taller1, taller2]:
        nombres = sistema.listar_participantes_taller(taller)
        print(f"{taller.nombre}: {', '.join(nombres) if nombres else 'ninguno'}")


if __name__ == "__main__":
    main()