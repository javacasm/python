class figura():
    def __init__(self, nombre_figura):
        self.nombre = nombre_figura
        
    def area(self):
        print('No esta definida')
        return 0.0
    
    def descripcion(self):
        return 'No esta definida'
    
    def __str__(self):
        return f'{self.nombre} {self.descripcion()} area:{self.area()}'

class rectangulo(figura):
    def __init__(self,longitud_lado1, longitud_lado2):
        super().__init__("rectangulo")
        self.lado1 = longitud_lado1
        self.lado2 = longitud_lado2
        
    def area(self):
        return self.lado1 * self.lado2
    
    def descripcion(self):
        return f'{self.lado1}x{self.lado2}'
    
class cuadrado(rectangulo):
    def __init__(self,longitud_lado):
        super().__init__(longitud_lado,longitud_lado)
        self.nombre ="cuadrado"
    
 
c = cuadrado(10)

print(c)

r = rectangulo(5,6)

print(r)