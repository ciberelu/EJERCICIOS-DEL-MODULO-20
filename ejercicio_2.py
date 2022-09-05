#Obtener los elementos impares de una lista pasado por parametro con filter y realizara una suma de todos estos 
#elementos obtenidos mediante reduce

from functools import reduce


lista = list (range(1, 101))

def imparesReduce (x):
    def impares (x):
        print (x)
        if x % 2 == 1:
            return True
        return False
    resultado = list(filter(impares, x))
    print(resultado)
    reducida = reduce( (lambda x, y: x + y), resultado)
    print(reducida) 


imparesReduce(lista)