class Student:
    School = "ABC"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
         return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.School
    @staticmethod
    def info():
        print("This is static Method")

s1 = Student(70, 80, 90)
s2 = Student(90, 100, 80)
print(s1.avg())
print(s2.avg())
print(Student.getschool())
Student.info()







