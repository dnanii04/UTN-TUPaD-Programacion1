#Ejercicio 3
"""
Ejercicio 3 (Alta) — “Agenda de Turnos con 
Nombres (sin listas)” 
Contexto 
Hay 2 días de atención: Lunes y Martes. 
Cada día tiene cupos fijos: 
• Lunes: 4 turnos 
• Martes: 3 turnos 
Reglas 
1. Pedir nombre del operador (solo letras). 
2. Menú repetitivo hasta salir: 
1. Reservar turno 
2. Cancelar turno (por nombre) 
3. Ver agenda del día 
4. Ver resumen general 
5. Cerrar sistema 
3. Reservar: 
o Elegir día (1=Lunes, 2=Martes). 
o Pedir nombre del paciente (solo letras). 
o Verificar que no esté repetido en ese día (comparando con las variables 
ya cargadas). 
o Guardar en el primer espacio libre (ej. lunes1, lunes2…). 
4. Cancelar: 
o Elegir día. 
o Pedir nombre del paciente (solo letras). 
o Si existe, cancelar y dejar el espacio vacío (""). 
5. Ver agenda del día: 
o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si 
está vacío. 
6. Resumen general: 
o Turnos ocupados y disponibles por día. 
o Día con más turnos (o empate). 
Restricciones 
• ❌ No listas, no diccionarios, no sets, no tuplas. 
• ✅ Se permite usar "" como “vacío”. 
• ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).
"""
#Validar nombre del operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: solo letras.")
    operador = input("Nombre del operador: ")

print(f"\nBienvenido, {operador}!")

#Variables de turnos (sin realizar listas)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

#Menú principal
salir = False

while not salir:
    print("\n1) Reservar  2) Cancelar  3) Ver agenda  4) Resumen  5) Cerrar")
    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción inválida.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    #RESERVAR
    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            #Verificar duplicado
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: ese paciente ya tiene turno el Lunes.")
            #Buscar primer espacio libre
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes, turno 1.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes, turno 2.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes, turno 3.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes, turno 4.")
            else:
                print("No hay turnos disponibles el Lunes.")

        else:  #dia == "2"
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: ese paciente ya tiene turno el Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes, turno 1.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes, turno 2.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes, turno 3.")
            else:
                print("No hay turnos disponibles el Martes.")

    #CANCELAR
    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        encontrado = False
        if dia == "1":
            if paciente == lunes1:
                lunes1 = ""
                encontrado = True
            elif paciente == lunes2:
                lunes2 = ""
                encontrado = True
            elif paciente == lunes3:
                lunes3 = ""
                encontrado = True
            elif paciente == lunes4:
                lunes4 = ""
                encontrado = True
        else:
            if paciente == martes1:
                martes1 = ""
                encontrado = True
            elif paciente == martes2:
                martes2 = ""
                encontrado = True
            elif paciente == martes3:
                martes3 = ""
                encontrado = True

        if encontrado:
            print(f"Turno de {paciente} cancelado.")
        else:
            print("Paciente no encontrado en ese día.")

    #VER AGENDA
    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error: ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\n── Agenda Lunes ──")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n── Agenda Martes ──")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    #RESUMEN GENERAL
    elif opcion == 4:
        #Contar ocupados
        ocup_lunes = 0
        if lunes1 != "": ocup_lunes += 1
        if lunes2 != "": ocup_lunes += 1
        if lunes3 != "": ocup_lunes += 1
        if lunes4 != "": ocup_lunes += 1

        ocup_martes = 0
        if martes1 != "": ocup_martes += 1
        if martes2 != "": ocup_martes += 1
        if martes3 != "": ocup_martes += 1

        print(f"\n── Resumen ──")
        print(f"Lunes  → Ocupados: {ocup_lunes} | Disponibles: {4 - ocup_lunes}")
        print(f"Martes → Ocupados: {ocup_martes} | Disponibles: {3 - ocup_martes}")

        if ocup_lunes > ocup_martes:
            print("Día con más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate en cantidad de turnos ocupados.")

    #CERRAR
    elif opcion == 5:
        print("Cerrando Sesión")
        salir = True
