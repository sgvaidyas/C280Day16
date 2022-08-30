class Employee():
    def __init__(self):
        self.id = 0
        self.name = ""

    def setdata(self):
        self.id = int(input("Enter the id = "))
        self.name = input("Enter the name = ")

    def getdata(self):
        return self.id,self.name

    def __str__(self):
        s = "ID  = " + str(self.id) + "\nNAME  = " +self.name
        return  s

ob = Employee()
#print(ob.getdata())
ob.setdata()
#print(ob.getdata())
print(ob)
