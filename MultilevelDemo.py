class A:
    def __init__(self):
        print("In A init")
    def Feature1(self):
        print("feature 1-A working")

class B:
    def __init__(self):
        print("In B init")
    def Feature1(self):
        print("feature 1-B working")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("In C init")
    def Feature1(self):
        super().Feature1()
        print("feature 1-C working")


c1 = C()
c1.Feature1()
