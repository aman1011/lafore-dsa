class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.nItems = 0

    
    def insert(self, item):
        self.__a[self.nItems] = item
        self.nItems += 1
    
    def delete(self, item):
        for j in range(self.nItems):
            if self.__a[j] == item:
                for k in range(j, self.nItems - 1):
                    self.__a[k] = self.__a[k+1]

                self.nItems -= 1
                return True
        
        return False
    
    def search(self, item):
        for j in range(self.nItems):
            if self.__a[j] == item:
                return j
        
        return False
    
    
    def traverse(self):
        for j in range(self.nItems):
            print(self.__a[j])

