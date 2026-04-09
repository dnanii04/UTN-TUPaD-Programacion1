#Ejercicio 4
"""
Ejercicio 4  — “Escape Room: La Bóveda” 
Historia 
Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo 
limitados. 
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás. 

Variables iniciales (NO se piden por teclado) 
• energia = 100 
• tiempo = 12 
• cerraduras_abiertas = 0 
• alarma = False 
• codigo_parcial = "" 
Validaciones obligatorias 
• No usar try/except. 
Pedir nombre del agente y validar con .isalpha() en un while. 
• Validar opciones del menú y cualquier número pedido con .isdigit() en un 
while. 
• El juego debe funcionar con estructuras secuenciales, condicionales y 
repetitivas (puede  usar funciones propias del lenguaje como .lower(), len(), 
formateo, etc.).

Regla anti-spam (muy importante) 
Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al 
iniciar: 
✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces: 
• se cobra el costo normal (-20 energía, -2 tiempo), 
• NO abre cerradura, y 
• se activa la alarma automáticamente (alarma = True) porque “la cerradura se 
trabó”. 
Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.

Menú de acciones (se repite mientras el juego siga) 
El juego continúa mientras: 
• energia > 0, tiempo > 0, cerraduras_abiertas < 3 
• y no esté bloqueado por alarma. 
En cada turno mostrar el estado y el siguiente menú: 
1. Forzar cerradura (costo: -20 energía, -2 tiempo) 
o Si la energía está por debajo de 40, hay “riesgo de alarma”: 
▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True. 
o Si no hay alarma, abre 1 cerradura. 
o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y 
no abre. 
2. Hackear panel (costo: -10 energía, -3 tiempo) 
o Debe usar un for de 4 pasos mostrando progreso. 
o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”). 
o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si 
todavía faltan. 

3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 
energía extra)

Regla de bloqueo por alarma 
• Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema 
se bloquea y se pierde. 

Condiciones de fin 
• Si cerraduras_abiertas == 3 → VICTORIA 
• Si energia <= 0 o tiempo <= 0 → DERROTA 
• Si se bloquea por alarma → DERROTA (bloqueo) 
"""
#Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
fuerzas_seguidas = 0 

#Validar nombre del agente
nombre = input("Nombre del agente: ")
while not nombre.isalpha():
    print("Error: solo letras.")
    nombre = input("Nombre del agente: ")

print(f"\n¡Bienvenido, agente {nombre}! La misión comienza...")

#Ciclo principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    #Verificar bloqueo por alarma al inicio del turno
    if alarma and tiempo <= 3:
        print("\nALARMA ACTIVA y tiempo crítico. Sistema bloqueado.")
        break

    #Mostrar estado actual
    print(f"\n{'='*45}")
    print(f"Agente: {nombre}")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVA' if alarma else 'Inactiva'} | Código: {codigo_parcial}")
    print(f"{'='*45}")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")

    #Validar opción del menú
    opcion = input("Acción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese 1, 2 o 3.")
        opcion = input("Acción: ")
    opcion = int(opcion)

    #OPCIÓN 1: Forzar cerradura
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        fuerzas_seguidas += 1
        print(f"\nForzando cerradura... (-20 energía, -2 tiempo)")

        #Regla anti-spam: 3 veces seguidas forzando
        if fuerzas_seguidas == 3:
            print("La cerradura se trabó por exceso de fuerza.")
            print("ALARMA ACTIVADA automáticamente.")
            alarma = True

        else:
            #Riesgo de alarma si la energía es menor a 40
            if energia < 40:
                print("Energía crítica. Riesgo de alarma.")
                riesgo = input("Elegí un número del 1 al 3: ")
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: ingrese 1, 2 o 3.")
                    riesgo = input("Elegí un número del 1 al 3: ")
                if int(riesgo) == 3:
                    print("ALARMA ACTIVADA por riesgo de energía.")
                    alarma = True
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura abierta. Total: {cerraduras_abiertas}/3")
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura abierta. Total: {cerraduras_abiertas}/3")

    #OPCIÓN 2: Hackear panel
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        fuerzas_seguidas = 0  #resetear contador anti-spam
        print("\nHackeando panel...")

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"  Paso {paso}/4 — Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"Código completo. Cerradura abierta automáticamente. Total: {cerraduras_abiertas}/3")

    #OPCIÓN 3: Descansar
    elif opcion == 3:
        fuerzas_seguidas = 0  # resetear contador anti-spam
        tiempo -= 1
        if alarma:
            energia -= 10
            print("\nDescansás, pero la alarma te drena energía extra. (-10 energía, -1 tiempo)")
        else:
            energia += 15
            if energia > 100:
                energia = 100
            print(f"\nDescansaste. (+15 energía, -1 tiempo) → Energía: {energia}")

#Condiciones de fin
print(f"\n{'='*45}")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! Agente {nombre} abrió la bóveda.")
elif alarma and tiempo <= 3:
    print(f"DERROTA — Sistema bloqueado por alarma.")
elif energia <= 0:
    print(f"DERROTA — Sin energía. Misión fallida.")
elif tiempo <= 0:
    print(f"DERROTA — Sin tiempo. Misión fallida.")
