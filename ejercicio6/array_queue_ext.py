from abc import ABC, abstractmethod
from collections.abc import Iterator
from data_structures import ArrayQueue
from array_queue_ext_abstract import ArrayQueueExtAbstract


class ArrayQueueExt(ArrayQueue, ArrayQueueExtAbstract):
    
    def __bool__(self) -> bool: 
        if self.is_empty():
            return True
        return False
    
    def __iter__(self) -> Iterator[T]: 
        pos = self._front
        for i in range(self._size):
            yield self._data[pos]
            pos = (pos + 1) % len(self._data)

    def __contains__(self, item: object) -> bool: 
        for elemento in self.__iter__():
            if elemento == item:
                return True
        return False
    

