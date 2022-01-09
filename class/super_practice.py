class A:
    def __init__(self):
        print("Unit 생성자")

class B:
    def __init__(self):
        print("Flyable 생성자")

class C(A, B):
    def __init__(self):
        #super().__init__()
        A.__init__(self)
        B.__init__(self)

# 드랍쉽
dropship = C()
# 두개 이상의 부모 클래스를 다중 상속 시 1번째 클래스를 상속받음