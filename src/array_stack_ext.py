from data_structures import ArrayStack
from array_stack_ext_abstract import ArrayStackExtAbstract

class ArrayStackExt[T](ArrayStackExtAbstract, ArrayStack):
    """Extensión de la clase ArrayStack que incorpora funcionalidades
    adicionales de iteración, búsqueda y manipulación de elementos"""

    def __init__(self, elems=None):
        super().__init__()

        if elems is not None:
            for elem in elems:
                self.push(elem)

    def __bool__(self):
        """Indica si la pila está vacía.
        Returns:
        bool: True si la pila está vacía, False en caso contrario."""
        return len(self) == 0

    def __iter__(self):
        """Devuelve un iterador que recorre los elementos de la pila
        desde el tope hacia la base
        Yields:
        T: Cada elemento almacenado en la pila"""
        for elem in reversed(self._data):
            yield elem

    def __contains__(self, item):
        """Indica si un elemento pertenece a la pila.
        Args:
        item (object): Elemento a buscar.
        Returns:
        bool: True si el elemento está en la pila,
        False en caso contrario."""
        for elem in self:
            if elem == item:
                return True
        return False

    def __reversed__(self):
        """Devuelve un iterador que recorre los elementos
        desde la base hacia el tope.
        Yields:
        T: Cada elemento almacenado en la pila
        en orden inverso."""
        for elem in self._data:
            yield elem

    def remove_first(self):
        """Elimina y devuelve el primer elemento de la pila,
        correspondiente a la base de la estructura.
        Returns:
        T: El primer elemento almacenado en la pila"""
        return self._data.pop(0)

    def remove_duplicates(self):
        """Elimina los elementos duplicados de la pila,
        conservando únicamente la primera aparición
        de cada elemento"""
        aux = set()
        resultado = []

        for elem in self._data:
            if elem not in aux:
                aux.add(elem)
                resultado.append(elem)

        self._data = resultado

    def __iadd__(self, other):
        """Agrega todos los elementos de otra pila
        al tope de la pila actual.
        Args:
        other (ArrayStack[T]): Pila cuyos elementos
            serán agregados.
        Returns:
        ArrayStackExt[T]: La pila actual modificada"""
        for elem in other:
            self.push(elem)

        return self