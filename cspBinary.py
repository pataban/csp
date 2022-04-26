from typing import OrderedDict
from csp import Csp
from support import *

class CspBinary(Csp):
    def __init__(self, n,forwawrdChceck=True,filename=None):
        super().__init__(n,forwawrdChceck)
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

        self.setVariableQueue()


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

    def setVariableQueue(self):
        #mozliwa mapa gestosci liczona na podstawie liczby wymuszonych sasiadow
        # wtedy queue w kolejnosci od najwiekszej gestosci 
        for i in range(0,self.n):
            for j in range(0,self.n):
                if(len(self.domain[i,j])==1):
                    self.currV+=1
                    self.variableQueue[self.currV]=(i,j)
                    
        
        varQId=self.currV+1
        for i in range(0,self.n):
            for j in range(0,self.n):
                if(len(self.domain[i,j])!=1):
                    self.variableQueue[varQId]=(i,j)
                    varQId+=1

        # wymaga aby solution posiadalo null tam gdzie jeszcze nie ma nic przypisane
        """domSum=np.sum(self.domain,axis=1)
        rowDomLen=list(map(lambda ds:(ds[0],len(ds[1])),enumerate(domSum)))
        rowDomLen.sort(key=lambda r:r[1])

        for r in rowDomLen:
            for j in range(0,self.n):
                if(len(self.domain[r[0],j])!=1):
                    self.variableQueue[varQId]=(r[0],j)
                    varQId+=1"""

        """order=np.empty_like(self.solution)
        orderId=0
        for v in self.variableQueue:
            order[v[0],v[1]]=orderId
            orderId+=1
        prt2D(order)
        print("aaa")"""