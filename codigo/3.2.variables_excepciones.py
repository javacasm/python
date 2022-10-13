try:
    dividendo = float(input("introduzca el dividendo: "))
    divisor = float(input("Introduzca el divisor: "))
    resultado = dividendo/divisor
except Exception as e:
    print("Se ha producido un error")
    print(e)