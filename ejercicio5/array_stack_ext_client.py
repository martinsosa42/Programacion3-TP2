import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ejercicio 3-4'))

from array_stack_ext import ArrayStackExt

# Metodo init
pila = ArrayStackExt([1,2,3,4,5,5])
print("Pila creada:", pila)

# Metodo bool
print("Está vacía?", bool(pila))

# Metodo iter
print("Iterador:")
for elem in pila:
    print(elem)

# Metodo contains
print ("Está 6 en la pila?", 6 in pila)

# Metodo reversed
print("Pila a la reversa:")
for elem in reversed(pila):
    print(elem)

# Metodo removedor del primero
print("Primer elemento borrado de la pila:", pila.remove_first())
print("Resultado tras remover elemento:", pila)

# Metodo removedor de duplicados
pila.remove_duplicates()
print("Resultado de remover duplicados de la pila:", pila)

# Metodo iadd
pila2 = ArrayStackExt([6,7,8,9,10])
pila.__iadd__(pila2)
print("Pila después de método iadd:", pila)











