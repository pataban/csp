from csp import Csp
from support import *


class CspBinary(Csp):
    def __init__(self, n,filename=None):
        super().__init__(n)
        self.constraintRow=[]
        self.constraintCol=[]
        for i in range(0,n):
            self.constraintRow.append([CspBinary.constraintTrippleValueRepetition,CspBinary.constraintEqualNumberSplit])
            self.constraintCol.append([CspBinary.constraintTrippleValueRepetition,CspBinary.constraintEqualNumberSplit])
        self.constraintGlobal=[CspBinary.constraintUniqueRowCol]
        
        if filename is None:
            self.setDomain([0,1])
        else:
            self.loadDomainBinary(filename)

    def constraintTrippleValueRepetition(data,currId):
        start(8)
        if(currId<2):
            return True
        if data[currId]==data[currId-1] and data[currId-1]==data[currId-2]:
            stop(8)
            return False

        """for d1,d2,d3 in zip(data,data[1:],data[2:]):
            if(d1==d2 and d2==d3):
                stop(8)
                return False    #chk time performance"""

        """for i in range(0,len(data)-2):
            if(data[i]==data[i+1] and data[i+1]==data[i+2]):
                stop(8)
                return False"""
        stop(8)
        return True

    def constraintUniqueRowCol(data,currX,currY):
        start(9)
        if(currX+1==data.shape[0]):
            for j in range(0,currY):
                if(np.array_equal(data[:,currY],data[:,j])):
                    stop(9)
                    return False
        if(currY+1==data.shape[1]):
            for j in range(0,currX):
                if(np.array_equal(data[currX,:],data[j,:])):
                    stop(9)
                    return False
        stop(9)
        return True

    def constraintEqualNumberSplit(data,currId):           ##chk tylko dla pelnego solution
        """for i in range(0,data.shape[0]):
            countZero=0
            countOne=0
            for j in range(0,data.shape[1]):#sum tablicy zamiast sprawdzania
                if data[i][j] ==0:
                    countZero+=1
                elif data[i][j] ==1:
                    countOne+=1
            if countZero!=countOne:
                return False
        for i in range(0,data.shape[1]):
            countZero=0
            countOne=0
            for j in range(0,data.shape[0]):
                if data[j][i] ==0:
                    countZero+=1
                elif data[j][i] ==1:
                    countOne+=1
            if countZero!=countOne:
                return False
        return True"""##porownac czas wykonania
        """ax0=np.sum(data,axis=0)
        for sum in ax0:
            if(sum<<1!=data.shape[0]):   #bit shift
                return False

        ax1=np.sum(data,axis=1)
        for sum in ax1:
            if(sum<<1!=data.shape[0]):
                return False"""
        if currId+1!=data.shape[0]:
            #print(f"{currId} -> true")
            return True
        sum=np.sum(data)
        #print(f"{data} -> {currId} -> {sum}")
        if(sum<<1!=currId+1):   #bit shift
            #print("false")
            return False
        #print("true")
        return True



    def loadDomainBinary(self,filename):
        self.domain=[]
        for i in range(0,self.n):
            self.domain.append([])
            for j in range(0,self.n):
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






















