class Student:
    def __init__(self, x, y):
        r = x+y
        print(r)
    def add(self, a=None, b=None, c=None):
        s = 0
        if a!= None and b!=None and c!=None :
            s = a+b+c
        elif a!=None and b!=None :
            s = a+b
        else :
            s = a
        print(s)
        return s

s1=Student(13, 14)
print(s1.add(4, 9, 6))

