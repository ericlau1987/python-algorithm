class linkedList:
# This class is used internally by the LinkedList class. It is 4     
# invisible from outside this class due to the two underscores 5     
# that precede the class name. Python mangles names so that they 6    
# are not recognizable outside the class when two underscores 7     
# precede a name but aren’t followed by two underscores at the 8     
# end of the name (i.e. an operator name).
    class __Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next 

        def getItem(self):
            return self.item 
        
        def getNext(self):
            return self.next 
        
        def setItem(self, item):
            self.item = item 

        def setNext(self, next):
            self.next = next        

    def __init__(self, contents=[]):
        self.first = linkedList.__Node(None, None)
        self.last = self.first 
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getItem__(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()
        
    def __setItem__(self, index, val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            self.setItem(val)
            return 
        return IndexError("LinkedList assignment index out of range")
    
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                str(type(self)) + " + " + str(type(other)))
        
        result = linkedList()

        cursor = self.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext() 

        cursor = other.first.getNext()

        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext() 

        return result


# def main():
#     print(linkedList([1,2,3]))