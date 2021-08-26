# -*- coding: utf-8 -*-
#Indice de listas
lista = [1, 3,4,5, True, "Hola"]
lista [0] 
print (lista [0])
print (lista [-1])
print (lista [0:2])
print (lista [0:-1])
# Comparaciones numéricas
a = 4
b = 5
print (a  >= b)

#Comparaciones Booleanas
print( a <= 5 and a > b)
print (not (a <= 5 and a > b)) #or, not

# Abrir archivos
archivo = r'E:\Fernandita_\MiPython\MisFilesTests\ciudades.txt'          # Ubicacion del archivo es una variable
with open (archivo, 'r') as f:   # definir el tipo de trabajo q hará el archivo - r -read
    data = f.read()   # Un bloque de código solo se lo limita con los espacios

print(data) 

# Toma de decisiones  (if - else)   Si la variable cumple una u otra o ninguna condicion, aplicar las diferentes secciones del código
numero_1 = 4
numero_2 = 8

if numero_1 > numero_2:
    print('')

