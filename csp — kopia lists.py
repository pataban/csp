from pandas import DataFrame
import copy
import numpy as np

def binaryRowColConstraint(data):
    #if(len(data)<3):        #usunac dla przyspieszenia
    #    return True
    for i in range(0,len(data)-2):
        if(data[i]==data[i+1] and data[i+1]==data[i+2]):
            return False
    return True

def binaryGlobalConstraint(data):
    pass

constraintRow=[binaryRowColConstraint,binaryRowColConstraint,binaryRowColConstraint,binaryRowColConstraint]
constraintCol=[binaryRowColConstraint,binaryRowColConstraint,binaryRowColConstraint,binaryRowColConstraint]
constraintGlobal=[]


class Csp():
    def __init__(self, n):
        self.n=n
        self.solution=np.empty((n,n))
        self.setupSolution()
        self.solutions=[]
        self.solutionCount=0
        self.domain=[]
        self.currX=0
        self.currY=-1

    def setDomain(self,domain):
        for i in range(0,self.n):
            self.domain.append([])
            for j in range(0,self.n):
                self.domain[i].append(domain)
    
    def loadDomainBinary(self,filename,domain):
        self.setDomain(domain)
        file=open(filename)
        for i in range(0,self.n):
            line=file.readline()
            for j in range(0,len(line)):
                if(line[j]=='1'):
                    self.domain[i][j]=[1]
                elif(line[j]=='0'):
                    self.domain[i][j]=[0]

    def setupSolution(self):
        for i in range(0,self.n):
            self.solution.append([])
            for j in range(0,self.n):
                self.solution[i].append(None)


    def nextSolution(self)->bool:   #false on finished all
        if((self.currX+1==self.n) and (self.currY+1==self.n)):  #full
            return self.backTrack()
        self.currY+=1
        if(self.currY>=self.n):
            self.currY=0
            self.currX+=1
        if(self.solution[self.currX][self.currY] is None):
            self.solution[self.currX][self.currY]=0
        return True    


    def mapSolution(self,solution):
        data=list(map(lambda sol,dom:list(map(lambda s,d:None if(s==None) else d[s],sol,dom)),solution,self.domain))
        """for it in (self.solution,self.domain):
            print(it)
            list(map(lambda s,d:print(d),it[0],it[1]))
            list(map(lambda s,d:print(d[s]),it[0],it[1]))
            data.append(list(map(lambda s,d:d[s],it[0],it[1])))"""
        return data

    def column(self,matrix, i):
        return [row[i] for row in matrix]

    def chkSolution(self)->bool:            #todo verivy
        mappedSolution=self.mapSolution(self.solution)
        for conR,mSol in zip(constraintRow,mappedSolution):
            if(not conR(mSol)):
                return False
        """for i in range(0,len(constraintRow)):
            if(not constraintRow[i](mappedSolution[i][:])):
                return False"""
        for i in range(0,len(constraintCol)):
            #if(i==0):
                #self.prtSolution()
                #print(self.solution[i][:])
                #print(self.solution[:][i])
                #print(self.column(mappedSolution,i))
                #print(list(map(lambda sol:sol[i],mappedSolution)))
                #input('')
            if(not constraintCol[i](list(map(lambda sol:sol[i],mappedSolution)))):
                return False
        for conG in constraintRow:
            if(not conG(mappedSolution)):
                return False
        if((self.currX+1==self.n) and (self.currY+1==self.n)):  #success #tylko 1 rozwiazanie
            self.solutionCount+=1
            if(self.solutionCount==1):
                self.solutions.append(copy.deepcopy(self.solution))
                self.prtSolution()
            return self.backTrack()
        return True
        

    def backTrack(self)-> bool: #false on finished all
        while(self.solution[self.currX][self.currY]+1>=len(self.domain[self.currX][self.currY])):
            if(self.currY>0):
                self.solution[self.currX][self.currY]=None
                self.currY-=1
            elif(self.currX>0):
                self.solution[self.currX][self.currY]=None
                self.currY=self.n-1
                self.currX-=1
            else:
                return False
        self.solution[self.currX][self.currY]+=1
        return True

    def prt2D(self,data):
        columns=[]
        for i in range(0,self.n):
            columns.append(' ')
        index=[]
        for i in range(0,self.n):
            index.append(' ')
        #tupleDomain=map(lambda dom: (lambda d:tuple(d),dom),domain)
        print(DataFrame(data,columns=columns,index=index))

    def prtSolution(self):
        self.prt2D(self.solution)

    def prtMappedSolution(self):
        self.prt2D(self.mapSolution(self.solution))
    
    def prtDomain(self):
        self.prt2D(self.domain)

if __name__ == "__main__":
    csp=Csp(6)
    csp.loadDomainBinary(r"dane\binary_6x6",[0,1])
    csp.prtDomain()
    #csp.prtSolution()

    while(csp.nextSolution()):
        if(csp.chkSolution()):
            pass#print('qwe')
        #if(csp.chkSolution()):
    
    print(len(csp.solutions))
    csp.solution=csp.solutions[0]
    csp.prtSolution()
    #print(csp.chkSolution())
    """for i in range(0,len(csp.solutions)):
        csp.solution=csp.solutions[i]
        csp.prtSolution()
        print(csp.chkSolution())"""

