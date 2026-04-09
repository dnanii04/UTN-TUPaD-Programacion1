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
