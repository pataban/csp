from csp import Csp
from support import *

class CspBinary(Csp):
    def __init__(self, n,filename=None):
        super().__init__(n)
        self.constraintRow=[]
        self.constraintCol=[]
        for _ in range(0,n):
            self.constraintRow.append([CspBinary.constraintTrippleValueRepetition,CspBinary.constraintEqualNumberSplit])
            self.constraintCol.append([CspBinary.constraintTrippleValueRepetition,CspBinary.constraintEqualNumberSplit])
        self.constraintGlobal=[CspBinary.constraintUniqueRowCol]
        
        if filename is None:
            self.setDomain([0,1])
        else:
            self.loadDomainBinary(filename)


    def constraintTrippleValueRepetition(data,currId)->bool:
        start("conTripple")
        if(currId<2):
            return True
        if data[currId]==data[currId-1] and data[currId-1]==data[currId-2]:
            stop("conTripple")
            return False
        return True

    def constraintEqualNumberSplit(data,currId)->bool:    
        start("conEqSplit")
        if currId+1!=data.shape[0]:
            stop("conEqSplit")
            return True
        if((np.sum(data)<<1)!=currId+1):   #bit shift
            stop("conEqSplit")
            return False
        stop("conEqSplit")
        return True

    def constraintUniqueRowCol(data,currX,currY)->bool:
        start("conUnique")
        if(currX+1==data.shape[0]):
            for i in range(0,currY):
                if(np.array_equal(data[:,currY],data[:,i])):
                    stop("conUnique")
                    return False
        if(currY+1==data.shape[1]):
            for i in range(0,currX):
                if(np.array_equal(data[currX,:],data[i,:])):
                    stop("conUnique")
                    return False
        stop("conUnique")
        return True


    def loadDomainBinary(self,filename):
        start("load")
        self.domain=[]
        for i in range(0,self.n):
            self.domain.append([])
            for _ in range(0,self.n):
                self.domain[i].append([0,1])

        file=open(filename)
        for i in range(0,self.n):
            line=file.readline()
            for j in range(0,len(line)):
                if(line[j]=='1'):
                    self.domain[i][j]=[1]
                elif(line[j]=='0'):
                    self.domain[i][j]=[0]
        
        self.domain=np.array(self.domain,dtype=list)
        self.mapSolution()
        stop("load")


