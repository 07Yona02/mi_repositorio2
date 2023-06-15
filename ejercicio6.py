# Crear un programa que convierta un número entero (mayor que 1 y menor o igual
# que 1000) a número romano.
# Análisis
# Inicializamos 3 vectores de 10 elementos, con los números romanos correspondientes
# a las unidades, decenas y centenas.
# Calculamos el número de centenas que tiene el número, y mostramos el número romano
# Calculamos el número de decenas que tiene el número, y mostramos el número romano
# Calculamos el número de unidades que tiene el número, y mostramos el número romano

# Inicializamos 3 listas, con los números romanos correspondientes
# a las unidades, decenas y centenas.
nu = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
nd = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
nc = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
#  leer el número
while True:
    num = int(input("Ingrese un número entre 1 y 1000:"))
    if num > 0 and num <= 1000:
        break
# Si el numero es 1000 mostramos el número romano M
if num == 1000:
    print("M")
else:
    # Calculamos las centenas,decenas y unidades.
    centenas = num // 100
    decenas = (num // 10) % 10
    unidades = num % 10
    # Mostramos los números romanos correspondientes.
    print(nc[centenas], nd[decenas], nu[unidades])


# Inicializamos 3 listas con los números romanos correspondientes a las unidades, decenas y centenas.
unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

# Leer el número
while True:
    num = int(input("Ingrese un número entre 1 y 1000: "))
    if 1 <= num <= 1000:
        break

# Inicializamos la variable para almacenar el número romano
numero_romano = ""

# Si el número es 1000, mostramos el número romano "M"
if num == 1000:
    numero_romano = "M"
else:
    # Calculamos las centenas, decenas y unidades
    centenas_num = num // 100
    decenas_num = (num // 10) % 10
    unidades_num = num % 10

    # Construimos el número romano agregando las partes correspondientes
    numero_romano += centenas[centenas_num]
    numero_romano += decenas[decenas_num]
    numero_romano += unidades[unidades_num]

# Mostramos el número romano
print("El número romano correspondiente es:", numero_romano)

# se han realizado los siguientes cambios:
# Se modificaron los nombres de las listas para que sean más descriptivos.
# Se ajustaron los espacios en la entrada del número para que sea coherente con el resto del código.
# Se agregó una variable numero_romano para almacenar el número romano construido.
# Se utilizó el operador de concatenación (+=) para construir el número romano agregando las partes correspondientes.
# Se agregó un mensaje para mostrar el número romano resultante.
# Estas mejoras hacen que el código sea más legible y eficiente.
