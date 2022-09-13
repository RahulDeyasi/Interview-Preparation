class matrix:
    def __init__(self):
        self.matrics=[]
    def matrixInput(self,row,col):
        for i in range(row):
            a=[]
            for j in range(col):
                a.append(int(input()))
            self.matrics.append(a)
    '''print matrix'''
    def printMatrix(self):
        for i in range(row):
            for j in range(col):
                print(self.matrics[i][j],end=" ")
    def printSpiral(self):
        sRow=0
        sCol=0
        m=len(self.matrics)
        n=len(self.matrics[0])
        eRow=m
        eCol=n
        while(sRow<eRow and sCol<eCol):
            for i in range(sCol,eCol):
                print(self.matrics[sRow][i],end=" ")
            sRow+=1
            for i in range(sRow,eRow,):
                print(self.matrics[i][eCol-1],end=" ")
            eCol-=1
            if sRow<eRow:
                for i in range(eCol-1,sCol-1,-1):
                    print(self.matrics[eRow-1][i],end=" ")
                eRow-=1
            if sCol<eCol:
                for i in range(eRow-1,sRow-1,-1):
                    print(self.matrics[i][sRow],end=" ")
                sCol+=1
                

if __name__=="__main__":
    row=int(input("Enter no. of rows"))
    col=int(input("Enter no.of cols"))
    mat=matrix()
    mat.matrixInput(row,col)
    mat.printSpiral()
    


