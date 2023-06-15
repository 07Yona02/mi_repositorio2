#Mª Luisa Trassierra n²

# Realizar un programa que pida un mes y un año (superior a 1900) y muestre el
# calendario del mes
import calendar
import re
from termcolor import colored


def solicitar_año():
    while True:
        try:
            year = int(input("Ingresa un año superior a 1900: "))
            if year > 1900:
                return year
        except ValueError:
            print("No has ingresado un número válido.")
        print("El año debe ser superior a 1900. Inténtalo de nuevo.")

def solicitar_mes():
    while True:
        try:
            mes =
            if 1 <= mes <= 12: int(input('Introduce un mes: '))
                return mes
            else:
                print('El mes debe estar entre 1 y 12.')
        except ValueError:
            print('No has ingresado un número')

def solicitar_dia():
    while True:
        try:
            dia = input('Dime un dia: ')
            if 1<= int(dia) <= calendar.monthrange(year, month)[1]:
                return str(dia)
            else:
                print('El dia introducido no existe en este mes.')
        except ValueError:
            print('No has introducido un número.')



cl = calendar.TextCalendar()
year = solicitar_año()
month = solicitar_mes()
day = solicitar_dia()

calendario_sep = cl.formatmonth(year, month)

patron_dia = r"\b{}\b".format(day)
calendario_sep_resaltado = re.sub(patron_dia, colored(day,"red"), calendario_sep)

print(calendario_sep_resaltado)