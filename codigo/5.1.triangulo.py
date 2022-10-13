try:
    altura= int(input("altura del triangulo: "))
    for i in range(1,altura+1):
        print("*" * i)
except Exception as e:
    print("Error: ",e)