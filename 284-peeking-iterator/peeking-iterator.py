class PeekingIterator:
    def __init__(self, iterator):

        self.iterator = iterator
        if self.iterator.hasNext():
            self.current = self.iterator.next() 
        else:
            self.current = None        

    def peek(self):

        return self.current
        

    def next(self):

        value = self.current
        if self.iterator.hasNext():
            self.current = self.iterator.next()  
        else: 
            self.current = None       
        return value
            
    def hasNext(self):

        return self.current != None
        