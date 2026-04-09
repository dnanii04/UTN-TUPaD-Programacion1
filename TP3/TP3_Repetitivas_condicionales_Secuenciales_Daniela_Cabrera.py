#Trabajo Práctico N°3- Repetitivas, Condicionales y Secuenciales
#Daniela Cabrera, Comisión 14

#Ejercicio 1
"""
Ejercicio 1— “Caja del Kiosco” 
Objetivo: Simular una compra con validaciones y cálculo de total. 
Requisitos 
1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). 
2. Pedir cantidad de productos a comprar (número entero positivo, validar con 
.isdigit() en while). 
3. Por cada producto (usar for): 
o Pedir precio (entero, validar .isdigit()). 
o Pedir si tiene descuento S/N (validar con while, aceptar s o n en 
cualquier mayuscula/minuscula). 
o Si tiene descuento: aplicar 10% al precio de ese producto. 
4. Al final mostrar: 
o Total sin descuentos 
o Total con descuentos 
o Ahorro total 
o Promedio por producto (usar float y formatear con :.2f, ejem: 
x = 3.14159 
print(f"{x:.2f}")) 
Validaciones obligatorias 
• Sin try/except. 
• No aceptar vacío en nombre (si queda vacío, es error). 
• Cantidad > 0 (si ingresa 0, volver a pedir). 
Salida esperada (ejemplo) 
Cliente: Ana 
Cantidad de productos: 3 
Producto 1 - Precio: 100  Descuento (S/N): s 
Producto 2 - Precio: 50   Descuento (S/N): n 
Producto 3 - Precio: 200  Descuento (S/N): s 
Total sin descuentos: $350 
Total con descuentos: $320.00 
Ahorro: $30.00 
Promedio por producto: $106.67 
"""

#Pedir el nombre del cliente
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: el nombre solo puede contener letras.")
    nombre = input("Cliente: ")

#Pedir cantidad de productos que va a comprar
cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) == 0:
    print("Error: ingrese un número entero positivo mayor a 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)

#Acumuladores para realizar el descuento o no
total_sin_desc = 0
total_con_desc = 0.0

#Realizar un bucle para cada producto 
for i in range(1, cantidad + 1):

    #Validar el precio
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        print("Error: ingrese un precio entero válido.")
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)

    #Validar descuento S/N
    descuento = input(f"Descuento (S/N): ")
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input(f"Descuento (S/N): ")

    #Aplicar descuento si corresponde
    if descuento.lower() == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_sin_desc += precio
    total_con_desc += precio_final

#Calcular el descuento y sacar el promedio
ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print(f"\nTotal sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


#Ejercicio 2
"""
Ejercicio 2  — “Acceso al Campus y Menú Seguro” 
Objetivo: Login con intentos + menú de acciones con validación estricta. 
Requisitos 
1. Definir credenciales fijas en el código: 
o usuario correcto: "alumno" 
o clave correcta: "python123" 
2. Permitir máximo 3 intentos para ingresar usuario y clave. 
3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 
4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 
1. Ver estado de inscripción (mostrar “Inscripto”) 
2. Cambiar clave (pedir nueva clave y confirmación; deben 
coincidir) 
3. Mostrar mensaje motivacional (1 frase) 
4. Salir 
5. Validación del menú: 
o Debe ser número (.isdigit()) 
o Debe estar entre 1 y 4 
Cambio de clave 
• La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, 
rechazar. 
Salida esperada  
Intento 1/3 - Usuario: alumno 
Clave: xxx 
Error: credenciales inválidas. 
Intento 2/3 - Usuario: alumno 
Clave: python123 
Acceso concedido. 
1) Estado  2) Cambiar clave  3) Mensaje  4) Salir 
Opción: a 
Error: ingrese un número válido. 
Opción: 5 
Error: opción fuera de rango.
Opción: 2 
Nueva clave: 123 
Error: mínimo 6 caracteres. 
"""
#Definir credenciales fijas
usuario_correcto = "alumno"
clave_correcta   = "python123"

#Bloque 1: Iniciar sesión con un máximo de 3 intentos 
intentos = 0
acceso   = False

while intentos < 3 and not acceso:
    intentos += 1
    print(f"\nIntento {intentos}/3")
    usuario = input("Usuario: ")
    clave   = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
    else:
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada.")

#Bloque 2: Menú (solo si se logró acceder)
if acceso:
    print("\nAcceso concedido.")
    clave_actual = clave_correcta   #Guardamos la clave para poder cambiarla

    salir = False
    while not salir:

        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")

        #Validar opción del menú
        opcion = input("Opción: ")
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            #Validar longitud mínima de nueva clave
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            #Validar que la confirmación coincida
            confirmar = input("Confirmar clave: ")
            while confirmar != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmar = input("Confirmar clave: ")

            clave_actual = nueva_clave
            print("✅ Clave actualizada correctamente.")

        elif opcion == 3:
            print("¡Cada línea de código te acerca más a tu meta!")

        elif opcion == 4:
            print("Cerrando sesión")
            salir = True



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

""" 
4. Ejemplo de Ejecución (Consola)  
Plaintext  --- BIENVENIDO A LA ARENA ---  
Nombre del Gladiador: Leonidas1  
Error: Solo se permiten letras.  
Nombre del Gladiador: Leonidas  
=== INICIO DEL COMBATE ===  
Leonidas (HP: 100) vs Enemigo (HP: 100) | Pociones: 3  
Elige acción:  
1. Ataque Pesado  
2. Ráfaga Veloz  
3. Curar  
Opción: A  
Error: Ingrese un número válido.  
Opción: 2  
>> ¡Inicias una ráfaga de golpes!  
> Golpe conectado por 5 de daño  
> Golpe conectado por 5 de daño  
> Golpe conectado por 5 de daño  
>> ¡El enemigo contraataca por 12 puntos!  
=== NUEVO TURNO ===  
Leonidas (HP: 88) vs Enemigo (HP: 85) | Pociones: 3
"""