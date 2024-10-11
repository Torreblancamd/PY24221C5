
"""
nombre_producto = input("Ingresa el nombre del producto")
stock = int(input("Ingresa la cantidad de unidades"))


if stock > 0:
    print(f"Tenes stock de este producto {nombre_producto}")
else:
   print(f"No tenes stock de este producto {nombre_producto}, reponer stock")
"""





nombre_producto = input("Ingresa el nombre del producto")
cant_unidades = int(input("Ingresa la cantidad de unidades"))
stock_producto =  10



if stock_producto >= cant_unidades:
    print(f"Unidades disponibles:  {stock_producto}")
    #ACTUALIZACION DE STOCK
    stock_producto = stock_producto - cant_unidades
    if stock_producto >= 5:
        print(f"Unidades disponibles:  {stock_producto}")
        print("No hace falta comprar nuevas unidades")
    else:
        print(f"Unidades disponibles:  {stock_producto}")
        print("Stock bajo, comprar nuevas unidades")

else:
   print(f"Unidades disponibles:  {stock_producto}")
   print("No se puede realizar la venta")