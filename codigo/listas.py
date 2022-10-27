>>> # Listas
>>> 
>>> dias_trabajo = [1,3,5,6,7,8,10]
>>> dias_trabajo.append(12)
>>> dias_trabajo.append(15)
>>> dias_trabajo
[1, 3, 5, 6, 7, 8, 10, 12, 15]
>>> dias_trabajo.remove(15)
>>> dias_trabajo
[1, 3, 5, 6, 7, 8, 10, 12]
>>> dias_trabajo[3]
6
>>> dias_trabajo.append(25)
>>> dias_trabajo.append(18)
>>> dias_trabajo.append(8)
>>> dias_trabajo
[1, 3, 5, 6, 7, 8, 10, 12, 25, 18, 8]
>>> dias_trabajo.sort()
>>> dias_trabajo
[1, 3, 5, 6, 7, 8, 8, 10, 12, 18, 25]
>>> dias_trabajo[6] = 9
>>> dias_trabajo
[1, 3, 5, 6, 7, 8, 9, 10, 12, 18, 25]
>>> dias_trabajo.insert(0,7)
>>> dias_trabajo
[7, 1, 3, 5, 6, 7, 8, 9, 10, 12, 18, 25]
>>> dias_trabajo.remove(7)
>>> dias_trabajo
[1, 3, 5, 6, 7, 8, 9, 10, 12, 18, 25]
>>> dias_trabajo.clear()
>>> dias_trabajo
[]
>>> dias_trabajo.insert(0,7)
>>> dias_trabajo.append(25)
>>> dias_trabajo.append(8)
>>> dias_trabajo
[7, 25, 8]
>>> dias_trabajo.append(9)
>>> dias_trabajo.append(2)
>>> dias_trabajo.append(1)
>>> dias_trabajo.append(22)
>>> dias_trabajo
[7, 25, 8, 9, 2, 1, 22]
>>> dias_trabajo[2]
8
>>> dias_trabajo[2:5]
[8, 9, 2]
>>> dias_trabajo.append('Pepito')
>>> dias_trabajo.append(3.14)
>>> dias_trabajo
[7, 25, 8, 9, 2, 1, 22, 'Pepito', 3.14]
>>> len(dias_trabajo)
9
>>> 
