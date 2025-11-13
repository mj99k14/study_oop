from typing

class Bar:
    def __init__(self,name:str) ->None:
        self.name:str = name
        
    @property
    def name(self):
        return self._name +"안녕하세요"
    
    @name.setter
    def name(self,value:str):
        self._name:str = value
    

obj = Bar("yc jung")
print(obj.name)