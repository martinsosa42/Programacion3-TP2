from abc import ABC, abstractmethod
from collections.abc import Iterator
from data_structures import ArrayQueue
from array_queue_ext_abstract import ArrayQueueExtAbstract


class ArrayQueueExt[T](ArrayQueue, ArrayQueueExtAbstract):
    
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
    def reverse_upto(self, k: int) -> None:
        if k < 0:
            raise ValueError("k no puede ser negativo")
        
        n = len(self)
        if n == 0 or k <= 1:
            return
        
        k = min(k, n)
        
        stack = []
        
        for _ in range(k):
            stack.append(self.dequeue())
            
        while stack:
            self.enqueue(stack.pop())
            
        for _ in range(n - k):
            item = self.dequeue()
            self.enqueue(item)
    def intercalar(self, queue: ArrayQueue[T]) -> None:

        n = len(self)
        
        for _ in range(n):

            self.enqueue(self.dequeue())
            
            if not queue.is_empty():
                self.enqueue(queue.dequeue())
        
        while not queue.is_empty():
            self.enqueue(queue.dequeue())