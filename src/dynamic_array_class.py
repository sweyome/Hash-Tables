class DynamicArray:
    def __init__(self,capacity = 8):
        self.length  = 0 
        self.capcity = capacity
        self.storage = [None] * capacity

    def insert(self,index, value):
        if self.length >= self.capcity:
            self.resize()

        # shift everything to the right of index, to the right 
        for i in range(self.length, -1):
            self.storage[i] = self.storage[i-1]

        # insert the value , at the index
        self.storage[index] = value
        self.length += 1

    def append(self, value):
        if self.length >= self.capcity:
            self.resize()
        self.storage[self.length] = value
        self.length += 1


    # write a function to resize our array automatically 

    def resize(self):
        # create a new Array, Bigger in Size
        self.capcity *=2 # double the Array size
        new_storage = [None] * self.capcity 
        # move all elements from old Array, into new one
        for i in range(self.length):
            new_storage[i] = self.storage[i]
        # set the mew array to storage
        self.storage = new_storage