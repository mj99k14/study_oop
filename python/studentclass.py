class student:
    count = 0
    def __init__(self,student_id,name,eng,kor,math):
        
        self.student_id =student_id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math =math
  
        student.count +=1
        
    def calc_total(self):
        self.total = self.eng + self.kor + self.math
        
    
    def calc_average(self ):
        self.average = self.total / 3
        

  
s1 = student("2025001", "Kim", 90, 80, 85)
s2 = student("2025002", "Lee", 70, 75, 80)

s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()
            
print(s1.student_id, s1.name, s1.total, s1.average)
print(s2.student_id, s2.name, s2.total, s2.average)

print("총 학생 수: ", student.count)
       