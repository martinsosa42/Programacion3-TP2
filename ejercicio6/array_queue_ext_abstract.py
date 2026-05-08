from abc import ABC, abstractmethod
from collections.abc import Iterator
from data_structures import ArrayQueue

class ArrayQueueExtAbstract[T](ABC):

    @abstractmethod
    def __bool__(self) -> bool: 
        """ Indica si la estructura está vacía o no.

        Returns:
            bool: retorna True si la estructura está vacía, False en caso contrario.
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]: 
        """ Devuelve un iterador que recorre los elementos en el orden que 
        establece la estructura.

        Yields:
            Iterator[T]: Un iterador que recorre los elementos.
        """
        pass

    @abstractmethod
    def __contains__(self, item: object) -> bool: 
        """ Indica si un elemento está en la estructura.

        Args:
            item (object): El elemento a buscar.

        Returns:
            bool: retorna True si el elemento está en la estructura, False en caso contrario.
        """
        pass
    
    @abstractmethod
    def reverse_upto(self, k: int) -> None: 
        """ Dado el entero k invertir el orden de los primeros k elementos de la cola, 
        dejando los demás elementos en el mismo orden relativo? Por ejemplo, si k=4 y
        la cola tiene los elementos [10, 20, 30, 40, 50, 60, 70, 80, 90], la salida 
        debería ser (40, 30, 20, 10, 50, 60, 70, 80, 90).

        Si k es mayor que la cantidad de elementos en la cola, se deben invertir todos los elementos.

        Raises:
            ValueError: Si k es negativo.

        Args:
            k (int): El número de elementos a invertir desde el frente de la cola.
        """
        pass

    @abstractmethod
    def intercalar(self, queue: ArrayQueue[T]) -> None: 
        """Modifica los elementos de la fila actual intercalándolos con los de la estructura pasada por parámetro.

        Args:
            queue (ArrayQueue[T]): La fila cuyos elementos se intercalarán con los de la fila actual.
        """
        pass