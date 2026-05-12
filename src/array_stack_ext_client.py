import sys
import os

#sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ejercicio 3-4'))

from array_stack_ext import ArrayStackExt

# Método init
pila = ArrayStackExt([1,2,3,4,5,5])
print("Pila creada:", pila)

# Método bool
print("Está vacía?", bool(pila))

# Método iter
print("Iterador:")
for elem in pila:
    print(elem)

# Método contains
print ("Está 6 en la pila?", 6 in pila)

# Método reversed
print("Pila a la reversa:")
for elem in reversed(pila):
    print(elem)

# Método removedor del primero
print("Primer elemento borrado de la pila:", pila.remove_first())
print("Resultado tras remover elemento:", pila)

# Método removedor de duplicados
pila.remove_duplicates()
print("Resultado de remover duplicados de la pila:", pila)

# Método iadd
pila2 = ArrayStackExt([6,7,8,9,10])
pila.__iadd__(pila2)
print("Pila después de método iadd:", pila)










