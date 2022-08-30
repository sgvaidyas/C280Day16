class MatrixOperations:
    def setdimension(self):
        self.rows = int(input("No of rows"))
        self.cols = int(input("No of cols"))

    def setdimensions(self):
        self.row1 = int(input("No of rows"))
        self.col1 = int(input("No of cols"))
        self.row2 = int(input("No of rows"))
        self.col2 = int(input("No of cols"))

    def setMatrix(self=None, r=0, c=0):
        mat = []
        for i in range(r):
            temp = []
            for j in range(c):
                ele = int(input("Enter ele = "))
                temp.append(ele)
            mat.append(temp)

        return mat

    def add2Matrix(self):
        self.mat1 = self.setMatrix(self.rows,self.cols)
        self.mat2 = self.setMatrix(self.rows,self.cols)
        self.res=[]
        for i in range(self.rows):
            temp=[]
            for j in range(self.cols):
                temp.append(self.mat1[i][j] + self.mat2[i][j])
                self.res.append(temp)

    def display(self):
        print("Matrix 1  = ")
        self.disp(self.mat1,self.rows,self.cols)
        print("Matrix 2  = ")
        self.disp(self.mat2,self.rows,self.cols)
        print("RES (ADDITION)  = ")
        self.disp(self.res,self.rows,self.cols)


    def disp(self,matrix,r=0,c=0):

        for i in range(r):
            for j in range(c):
                print(matrix[i][j] , end="\t")
            print()


    def mulMatrix(self):
        self.setdimensions()
        self.mat1 = self.setMatrix(self.row1,self.col1)
        self.mat2 = self.setMatrix(self.row2,self.col2)
        self.res = []
        if self.col1!=self.row2:
            print("Multiplication is not possible")
        else:
            for i in range(self.row1):
                temp = []
                for j in range(self.col2):
                    sum=0
                    for k in range(self.col1):
                        sum += self.mat1[i][k] * self.mat2[k][j]
                    temp.append(sum)
                self.res.append(temp)
            print("Matrix 1  = ")
            self.disp(self.mat1,self.row1,self.col1)
            print("Matrix 2  = ")
            self.disp(self.mat2,self.row2,self.col2)
            print("RES (ADDITION)  = ")
            self.disp(self.res,self.row1,self.col2)





ob = MatrixOperations()
#ob.setdimension()
#ob.add2Matrix()
#ob.display()
ob.mulMatrix()
