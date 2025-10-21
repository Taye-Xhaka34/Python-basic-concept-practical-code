class Student:
    school = 'Arbaminch Campus'
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        def avg(self):
            return(self.m1 + self.m2 + self.m3)/3
        @classmethod
        def getSchool(cls):
            return cls.school
        @staticmethod
        def info():
            print("This is student calss.. in abc module")
s1 = Student(34, 47, 32)
s2 = Student(89, 45, 77)
#print(s1.avg())
print(Student.getSchools()) 
Student.info()       