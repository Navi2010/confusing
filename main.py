class x:
    def __init__(self):
        print('i am the parent constructor')
    def y(self):
        print('i am the from the parent')

class a(x):
    def __init__(self):
        print('i am the child constructor')
        x.__init__(self)

ob1 = a()
ob1.y()

print(issubclass(a, x))
