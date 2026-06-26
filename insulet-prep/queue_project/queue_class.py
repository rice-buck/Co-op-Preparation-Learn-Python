#queue class to be used for all purposes

from collections import deque


class Queue: 

    #constructor
    def __init__(self):
        self.dq = deque() #intialize empty deque

    def enqueue(self, item):
        self.dq.appendleft(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cant remove from an empty queue")
        else:
            return self.dq.pop()
    
    def clear(self):
        self.dq.clear()

    def is_empty(self):
        return len(self.dq) == 0
    
    def print(self):
        print(self.dq)