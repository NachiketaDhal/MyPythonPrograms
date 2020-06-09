class Computer:
   def __init__(self):
       self .age = 18

   def compare(self, others):
       if self.age == others.age :
          return True
       else:
          return False

c1 = Computer()
c2 = Computer()
c1.age = 19
if c1.compare(c2):
    print("same age")
else:
    print("different age")

