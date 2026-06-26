#queue class to be used for all purposes

from collections import deque


class Queue: 

    #constructor
    def __init__(self):
        self.dq = deque() #intialize empty deque

    def enqueue(self, item):
        self.dq.appendleft(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Cant remove from an empty queue")
        else:
            return self.dq.pop()
    
    def clear(self):
        self.dq.clear()

    def is_empty(self):
        return len(self.dq) == 0
    
    def print(self):
        print(self.dq)


que1 = Queue()
que1.enqueue(1)
que1.enqueue(20)
que1.enqueue(80)
que1.enqueue("yes")
que1.print()

while True:
    user_input = input("Press 'D' to dequeue or 'E' to empty or 'Q' to quit")

    if user_input.lower().strip() == 'd':
        try: 
            removed = que1.dequeue()
            print("Removed {", removed, "}")
        except IndexError as e:
            print(e)
        que1.print()

    elif user_input.lower().strip() == 'e':
        que1.clear()
        que1.print()

    elif user_input.lower().strip() == 'q':
        print("Quiting")
        que1.print()
        break

if que1.is_empty():
    print("Empty")
else:
    print("Not empty")
