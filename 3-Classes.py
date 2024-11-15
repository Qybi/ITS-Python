class MyClass:
    myAttr = 10
    message = ''
    
    # constructor
    def __init__(self):
        print("Constructor called")
    
    # message getter and setter
    def getMessage(self):
        return self.message
    def setMessage(self, message):
        self.message = message
    
    # instance method
    def myMethod(self, message):
        print(message)
        
    # class method - it is a method that is bound to the class and not the object of the class, 
    # it can modify the class state that would apply across all instances of the class
    @classmethod
    def myClassMethod(cls, message):
        cls.setMessage(message)
        print(cls.getMessage())
    
    # static method - it is a method that is bound to the class and not the object of the class,
    # Myclass.add()
    @staticmethod
    def add(a, b):
        return a + b
        
    
        
myObject = MyClass()
myObject.myMethod("Hello World!") # this is equivalent to MyClass.myMethod(myObject, "Hello World!")

