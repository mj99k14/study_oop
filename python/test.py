class student:
    __id_count = 0
    def __init__(self,name,id,gender):
        self.name = name
        self.id =id
        self.gender = gender
        self.grade_korean = 0
        self.grande_math = 0
        self.grande_english = 0
        self.total = 0
        self.avg = 0
        student.__id_count +=1
        
    def set_score(self,korean,math,eng):
        self.grade_korean = korean
        self.grande_math = math
        self.grande_english = eng
        self.total =  (korean+math+eng)
        self.avg = (korean+math+eng)  /3
    
    def get_total_avg(self):
        return (self.total,self.avg)
    
    @classmethod
    def get_id_count(cls):
        return cls.__id_count
    
    @staticmethod
    def get_avg(korean,math,eng):
        return (korean+math+eng) /3