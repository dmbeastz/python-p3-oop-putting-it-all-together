#!/usr/bin/env python3

class Book:
    def __init__(self, title = "And Then They were none", page_count = 272):
        self.title = title
        self.__title = None
        self.__page_count = None
        self.page_count = page_count
    def get_page_count (self):
        return self.__page_count 
    def get_title (self):
        return self.__title
    def set_count (self,count):
        if type (count) == int:
            self.__page_count = count
        else:
            print("page_count must be an integer")
    def turn_page (self):
        print ("Flipping the page...wow, you read fast!")
    page_count = property(get_page_count,set_count)

    
    
        
  
    
        