class A:
    def feature1(self):
        print("feature1 is working")
class B:
    def feature2(self):
        print("feature2 is working")
class C(A,B):
    def feature3(self):
        print("feature3 is working")

c1=C()
c1.feature1()