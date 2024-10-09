

"""
edad_usuario = 15


if edad_usuario >= 18:
    print("Bienvenido/a al sistema")
    print("*Muestro el menu*")
else:
    print("No podes ingresar al sistema")




print("HOLA")

"""


"""
edad_usuario = 15
if edad_usuario >= 18:
    print("Bienvenido al sistema")
    print("muestro el menu*")
else:
    print("No podes ingresar al sistema")
"""



#Calculadora que suma o resta dos numeros


num_uno = "juan"
num_dos = 50

operacion = input("Ingrese la operacion: SUMA(+)  RESTA(-): ")



if operacion == "+" and type(num_uno) == int and type(num_dos) == int:
    resultado = num_uno + num_dos
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-" and type(num_uno) == int and type(num_dos) == int:
    resultado = num_uno - num_dos
    print(f"El resultado de la resta es: {resultado}")
else:    
    print(f"Operacion no encontrada {operacion}")




#OPERADORES LOGICOS: and---->Y  or----->O


#AND y
print( 30 > 20 and 50 == 50)#True
print( 40 < 30 and 60 == 50 + 10)#False


#OR o

print( 30 > 20 or 50 == 50)#True
print( 40 < 30 or 60 == 50 + 10)#True


