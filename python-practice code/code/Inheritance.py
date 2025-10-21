class A:
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")    
class B:
    def __init__(self):
        print("in B Init")
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
class C(A, B):
    def __init__(self):
        super().__init__()
    def feat(self):
        super().feature2()
a3 = C()
a3.feat()                        
