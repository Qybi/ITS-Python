class myClass:
    # class variable
    pepega = "pepega"
    
    def __init__(self, attr, message):  # constructor
        # instance variable
        self.__myAttr = attr
        self.message = message

    # getter/setter
    def get_attr(self):
        print(self.__myAttr)
        
    def set_attr(self, value):
        self.__myAttr = value
        
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, value):
        self.__message = value

myObject = myClass()
myObject.set_attr(10)
myObject.get_attr()