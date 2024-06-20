class Array(object):
    def __init__(self, initialMaxSize):
        self.__a = [None] * initialMaxSize
        self.__nItems = 0


    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    
    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                for k in range(j, self.__nItems - 1):
                    self.__a[k] = self.__a[k + 1]

                self.__nItems -= 1
                return True

        return False


    def search(self, item):
        return self.get(self.find(item))


    def traverse(self):
        for j in range(self.__nItems):
            print(self.__a[j])


    def get(self, n):
        if n >= 0 and n < self.__nItems:
            return self.__a[n] 
        return None


    def set(self, n, item):
        if n >= 0 and n < self.__nItems:
            self.__a[n] = item
            return True
        return False


    def __len__(self):
        return self.__nItems
    

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
            
        return -1
        