class BClass:
    def __init__(self):
        self.message = ''

# A class is inheriting from BClass - BClass is superclass of AClass
class AClass(BClass):
    def __init__(self):
        super().__init__() # calling base class constructor
        print("Constructor called")