class Bar:
    #.instance method
    def i_method(self):
        self.iValue = 20
    
    
    #class method    
    def c_method(cls):
        cls.cValue = 30
        
obj =Bar()
obj.i_method()
obj.c_method()