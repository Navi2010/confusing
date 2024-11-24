class bird:
    def __init__(self, name):
        self.name = name
    def x(self):
        print(self.name)

class pigeon(bird):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)
    def y(self):
        print(self.color)

ob1 = pigeon('gary', 'gray')
ob1.x()
ob1.y()        