class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        new_lst = []
        for i in range(self.frontIdx, len(self.items)):
            new_lst.append(self.items[i])

        self.items = new_lst
        self.frontIdx = 0

    def isEmpty(self):
        return self.frontIdx == len(self.items)

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")
        
        if self.frontIdx * 2 > len(self.items):
            self.__compress()

        # print(f'{self.frontIdx}; {self.items}; {self.isEmpty()}')
        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item 
    
    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")
        
        return self.items[self.frontIdx]
    
def main():
    q = Queue()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        q.enqueue(k)

    if q.front() == 0:
        print("Test 1 Passed")
    else:
        print("Test 1 failed")

    while not q.isEmpty():
        lst2.append(q.dequeue())
        print(f'{q.items}; {q.frontIdx}')

    if lst2 != lst:
        print("Test 2 Failed")
    else:
        print("Test 2 Passed")

if __name__ == "__main__":
    main()
