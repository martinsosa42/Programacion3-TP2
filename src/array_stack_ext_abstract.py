from abc import ABC, abstractmethod
from typing import Iterator
from data_structures import ArrayStack


class ArrayStackExtAbstract[T](ABC):
    @abstractmethod
    def __bool__(self) -> bool:
        """Indica si la estructura está vacía o no.
        Returns:
        bool: retorna True si la estructura está vacía, False en caso 
        contrario.
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
        """Indica si un elemento está en la estructura.
        Args:
            item (object): El elemento a buscar.
        Returns:
            bool: retorna True si el elemento está en la estructura, 
      False en caso contrario.
        """
        pass

    @abstractmethod
    def __reversed__(self) -> Iterator[T]:
        """ Devuelve un iterador que recorre los elementos en el orden inverso.
        Yields:
            Iterator[T]: Un iterador que recorre los elementos en orden inverso.
        """
        pass

    @abstractmethod
    def remove_first(self) -> T:
        """ Elimina y devuelve el primer elemento de la estructura.
        Returns:
            T: El primer elemento de la estructura.
        """
        pass

    @abstractmethod
    def remove_duplicates(self) -> None:
        """ Elimina los elementos duplicados de la estructura, dejando 
        solo una instancia de cada elemento. """
        pass

    @abstractmethod
    def __iadd__(self, other: ArrayStack[T]) -> None:
        """ Concatena todos los elementos de other al tope de la pila actual.
        Args:
            other (ArrayStack[T]): La pila cuyos elementos se agregarán 
            a la pila actual.
        """
        pass
