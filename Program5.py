class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setdata(self,a,b):
        self.x = a
        self.y = b

    def __str__(self):
        return   " x = " + str(self.x) + " y = "+ str(self.y)

    def compare(self,other):
        if self.x == other.x and self.y==other.y:
            return True
        return False

ob1 = Point()
ob2 = Point()
ob1.setdata(2,3)
ob2.setdata(22,3)
print(ob1)
print(ob2)
if ob1.compare(ob2):
    print("Ob1 and 2 are equal")
else:
    print("Ob1 and 2 are not equal")
