class Node:
    def __init__(self, value = None):
        self.prev = None
        self.next = None
        self.value = value

class MyCircularDeque:

    def __init__(self, k: int):
        self.maxLength = k
        self.counter = 0
        self.front = None
        self.rear = None
        

    def insertFront(self, value: int) -> bool:
        if self.counter == self.maxLength:
            return False
        newFront = Node(value)
        if self.counter == 0:
            self.front = self.rear = newFront
            self.front.next = self.rear
            self.front.prev = self.rear
            self.rear.next = self.front
            self.rear.prev = self.front
        else:
            newFront.next = self.front
            newFront.prev = self.rear
            self.front.prev = newFront
            self.rear.next = newFront
            self.front = newFront
        self.counter += 1
        
        return True


    def insertLast(self, value: int) -> bool:
        if self.counter == self.maxLength:
            return False
        newRear = Node(value)
        if self.counter == 0:
            self.front = self.rear = newRear
            self.front.next = self.rear
            self.front.prev = self.rear
            self.rear.next = self.front
            self.rear.prev = self.front
        else:
            newRear.prev = self.rear
            newRear.next = self.front
            self.front.prev = newRear
            self.rear.next = newRear
            self.rear = newRear
        self.counter += 1
        
        return True    


    def deleteFront(self) -> bool:
        if self.counter == 0:
            return False
        if self.counter == 1:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = self.rear
            self.rear.next = self.front

        self.counter -= 1
        return True


    def deleteLast(self) -> bool:
        if self.counter == 0:
            return False
        if self.counter == 1:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = self.front
            self.front.prev = self.rear
            
        self.counter -= 1
        return True


    def getFront(self) -> int:
        if self.counter == 0:
            return -1
        return self.front.value


    def getRear(self) -> int:
        if self.counter == 0:
            return -1
        return self.rear.value


    def isEmpty(self) -> bool:
        return (self.counter == 0)


    def isFull(self) -> bool:
        return (self.counter == self.maxLength)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()