#!/usr/bin/env python3

class Shoe:
    def __init__ (self, brand, size):
        self._brand = None
        self._size = None
        self.brand = brand
        self.size = size
        self.condition = "used"
    def get_size(self):
        return self._size
    def set_size(self,count):
        if type(count) == int:
            self._size = count
        else:   
            print("size must be an integer")
    size = property(get_size, set_size)
    def cobble(self):
       print("Your shoe is as good as new!")
       self.condition = "New"

    
   
        