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