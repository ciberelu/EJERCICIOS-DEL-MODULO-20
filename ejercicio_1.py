

from posixpath import split


paises_usuario = input("ingrese los paises separados por coma ")
paises_usuario = paises_usuario.split(", ")
sinRepetidos = []
for elemento in paises_usuario:
    if elemento not in sinRepetidos:
        
        sinRepetidos.append(elemento)

ordenado = sorted(sinRepetidos)
print(ordenado)
#usando set
sinRepetidosSet = set(paises_usuario)



ordenadoSet = sorted(sinRepetidosSet)

print(ordenadoSet)



