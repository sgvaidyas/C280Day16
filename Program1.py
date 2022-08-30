class Rectangle:
    #properties     -> data members
    #functionalities -> methods
    def setdata(self):
        self.leng = int(input("Enter the len = "))
        self.bred = int(input("Enter the bred = "))

    def calculate(self):
        self.area = self.leng*self.bred
        self.peri = 2*(self.leng+self.bred)

    def display(self):
        print("LENGTH       =     ",self.leng)
        print("BREADTH      =     ",self.bred)
        print("AREA         =     ",self.area)
        print("PERIMETER    =     ",self.peri)

ob = Rectangle()
ob.setdata()
ob.calculate()
ob.display()
print("-----------------------------")
ob1 = Rectangle()
Rectangle.setdata(ob1)
Rectangle.calculate(ob1)
Rectangle.display(ob1)
