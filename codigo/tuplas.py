>>> # Tuplas
>>> 
>>> dias_semana = ('L','M','X','J','V','S','D')
>>> 
>>> len(dias_semana)
7
>>> for dia in dias_semana:
    print(dia)
    
L
M
X
J
V
S
D
>>> 'M' in dias_semana
True
>>> dias_semana.find('M')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'find'
>>> dias_semana.index('M')
1
>>> dias_semana.index('S')
5
>>> dias_trabajo = ('L','M','X','L','X','J')
>>> dias_trabajo.index('L')
0
>>> dias_trabajo.count('L')
2
>>> dias_trabajo.count('M')
1
>>> dias_mes_trabajo = (1,4,5,6,7,10,12,3)
>>> dias_mes_trabajo[2]