#Ejercicio 5
"""
Ejercicio 5  — “Escape Room:"La Arena del 
Gladiador"  
1. Descripción del Escenario  
Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un 
usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El 
objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.  
Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de 
control (if/elif/else), ciclos (while y for) y validación de datos estricta.  
2. Requerimientos Técnicos  
A. Tipos de Datos  
Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:  
• • String: Para el nombre del jugador.  
• • Int: Para los Puntos de Vida (HP) y cantidad de pociones.  
• • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5). 
• Boolean: Para controlar si el juego sigue activo o quién tiene el turno.  
B. Reglas de Validación (¡Importante!)  
• • No está permitido usar bloques try / except.  
• • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.  
• • Para validar números, debes usar el método .isdigit() dentro de un ciclo 
while.  
3. Flujo del Programa  
Paso 1: Configuración del Personaje  
El programa inicia pidiendo el nombre del Gladiador.  
• • Validación: El nombre solo puede contener letras. Si el usuario ingresa números, 
símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a 
preguntar hasta que sea válido.  
Paso 2: Inicialización de Estadísticas
El programa debe definir las variables iniciales (sin preguntar al usuario):  
• • Vida del Gladiador: 100 (int)  
• • Vida del Enemigo: 100 (int)  
• • Pociones de Vida: 3 (int)  
• • Daño base "Ataque Pesado": 15 (int)  
• • Daño base del enemigo: 12 (int)  
• • Turno Gladiador : True (booleano)  
Paso 3: El Ciclo de Combate  
El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 
puntos de vida.  
Turno del Jugador:  
Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 
opciones:  
1. Ataque Pesado  
2. Ráfaga Veloz (Requiere uso de for)  
3. Curar  
• Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo 
ingresado sea un número (.isdigit()).  
2. Verificar que el número sea 1, 2 o 3.  
o Si falla alguna validación, mostrar mensaje de error y volver a pedir.  
Lógica de las Acciones:  
Acción A: Ataque Pesado (Opción 1)  
• • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador 
realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).  
• • Resta el daño a la vida del enemigo.  
• • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"  
Acción B: Ráfaga Veloz (Opción 2)  
• • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.  
• • El bucle debe repetirse 3 veces (usando range).  
• • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.  
• 2. Muestra el mensaje: " > Golpe conectado por 5 de daño".  
•  
Acción C: Curar (Opción 3)  
• Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.  
• • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el 
enemigo ataca igual).  
Turno del Enemigo:  
Justo después de tu acción, el enemigo ataca automáticamente.  
• • Resta el daño base del enemigo (12) a tu vida.  
• • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"  
Paso 4: Fin del Juego  
Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:  
• • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."  
• • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."  
"""
#Configurar el personaje 
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

#Variables iniciales (sin preguntar al usuario)
vida_jugador    = 100       # int
vida_enemigo    = 100       # int
pociones        = 3         # int
danio_pesado    = 15        # int
danio_enemigo   = 12        # int
turno_gladiador = True      # boolean
juego_activo    = True      # boolean

print(f"\n=== INICIO DEL COMBATE ===")

#Ciclo de combate
while vida_jugador > 0 and vida_enemigo > 0:

    # Mostrar estado actual
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # Validar opción del menú
    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Ingrese 1, 2 o 3.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    #Acción A: Ataque Pesado
    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = int(danio_pesado * 1.5)   # float → int para restar
            print(f"¡GOLPE CRÍTICO! Daño multiplicado x1.5 = {danio_pesado * 1.5}")
        else:
            danio_final = danio_pesado

        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    #Acción B: Ráfaga Veloz
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print(f"> Golpe conectado por 5 de daño")

    #Acción C: Curar
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Usaste una poción. +30 HP → Vida: {vida_jugador} | Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")

    #Turno del enemigo (si sigue vivo)
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")
    else:
        print("¡El enemigo ha caído!")

    #Separador de turno
    if vida_jugador > 0 and vida_enemigo > 0:
        print("\n=== NUEVO TURNO ===")

#Fin del juego
print(f"\n{'='*40}")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print(f"{'='*40}")