from pandas import DataFrame
import copy
import numpy as np
from support import *

class Csp():
    def __init__(self, n,forwawrdChceck=True):
        self.n=n
        self.forwawrdChceck=forwawrdChceck
        self.domain=None
        self.solution=np.full((n,n),0)
        self.solutions=[]
        self.solutionCount=0
        self.mappedSolution=None
        self.mappedSolutions=[]
        self.currX=0
        self.currY=-1
        self.constraintRow=[]
        self.constraintCol=[]
        self.constraintGlobal=[]
        self.constraintVariable=np.empty((n,n),dtype=list)
        for i in range(0,n):
            for j in range(0,n):
                self.constraintVariable[i,j]=[]
        self.variableQueue=np.empty(n*n,dtype=tuple)
        for i in range(0,n):
            for j in range(0,n):
                self.variableQueue[i*self.n+j]=(i,j)
        self.currV=-1


    def setDomain(self,domain):
        self.domain=[]
        for i in range(0,self.n):
            self.domain.append([])
            for _ in range(0,self.n):
                self.domain[i].append(domain)
        self.domain=np.array(self.domain,dtype=list)
        self.mapSolution()
  
    def mapSolution(self,solution=None):
        start("map")
        if (solution is None):
            solution=self.solution
        if(self.mappedSolution is None):
            self.mappedSolution=np.empty_like(solution)

        for i,(dom, sol) in enumerate(zip(self.domain,solution)):
            for j,(d,s) in enumerate(zip(dom,sol)):
                self.mappedSolution[i,j]=d[s]
        stop("map")
    
    def nextVariableId(self):
        if self.currV+1==self.n*self.n:
            return False
        self.currV+=1
        self.currX=self.variableQueue[self.currV][0]
        self.currY=self.variableQueue[self.currV][1]
        return True

    def prevVariableId(self):
        if self.currV==0:
            return False
        self.currV-=1
        self.currX=self.variableQueue[self.currV][0]
        self.currY=self.variableQueue[self.currV][1]
        return True

    def isFullSolution(self)->bool:
        return (self.currV+1==self.n*self.n)

    def chkConstraints(self)->bool:
        start("chkCon")
        #self.prtMappedSolution()
        #print(f"{self.currX} {self.currY}")

        start("chkConVar")
        for conV in self.constraintVariable[self.currX,self.currY]:
            if not conV(self.mappedSolution[self.currX,self.currY]):
                stop("chkCon")
                stop("chkConVar")
                #print("row false")
                return False        
        stop("chkConVar")

        start("chkConRow")
        for conR in self.constraintRow[self.currX]:
            if not conR(self.mappedSolution[self.currX],self.currY):
                stop("chkConRow")
                stop("chkCon")
                #print("row false")
                return False
        for conC in self.constraintCol[self.currY]:
            if not conC(self.mappedSolution[:,self.currY],self.currX):
                stop("chkConRow")
                stop("chkCon")
                #print("col false")
                return False
        stop("chkConRow")

        start("conG")
        for conG in self.constraintGlobal:
            if(not conG(self.mappedSolution,self.currX,self.currY)):
                stop("conG")
                stop("chkCon")
                #print("glo false")
                return False
        stop("conG")

        stop("chkCon")
        #print("true")
        return True

    def chkSolution(self)->bool:
        if self.isFullSolution() and self.chkConstraints():
            return True
        return False

    def saveSolution(self):
        start("save")
        self.solutionCount+=1
        self.solutions.append(copy.deepcopy(self.solution))
        self.mappedSolutions.append(copy.deepcopy(self.mappedSolution))
        stop("save")
  
    def nextVariable(self)->bool:
        start("nextV")
        if(self.isFullSolution()):
            stop("nextV")
            return self.backTrack()

        self.nextVariableId()
        self.solution[self.currX,self.currY]=0
        self.mappedSolution[self.currX,self.currY]=self.domain[self.currX,self.currY][0]
        self.valueSelected(self.currX,self.currY,self.mappedSolution[self.currX,self.currY])
        stop("nextV")
        return True        

    def backTrack(self)-> bool:
        start("backT")
        while(self.solution[self.currX][self.currY]+1>=len(self.domain[self.currX][self.currY])):
            self.valueUnSelected(self.currX,self.currY,self.mappedSolution[self.currX,self.currY])
            if not self.prevVariableId():     #no more possible solutions - completed 
                stop("backT")
                return False        
        self.valueUnSelected(self.currX,self.currY,self.mappedSolution[self.currX,self.currY])
        self.solution[self.currX,self.currY]+=1
        self.mappedSolution[self.currX,self.currY]=self.domain[self.currX,self.currY][self.solution[self.currX,self.currY]]
        self.valueSelected(self.currX,self.currY,self.mappedSolution[self.currX,self.currY])
        stop("backT")
        return True

    def valueSelected(self,x,y,value):
        pass

    def valueUnSelected(self,x,y,value):
        pass

    def getFirst(self)->bool:
        start("all")
        while self.nextVariable():
            while not self.isFullSolution():
                if self.chkConstraints():
                    #input()
                    self.nextVariable()
                else:
                    self.backTrack()
            if self.chkConstraints():
                self.saveSolution()
                stop("all")
                return True
            #input()
        stop("all")
        return False

    def getAll(self)->bool:
        found=False
        while(self.getFirst()):
            found=True
        return found
    
    def prtSolution(self):
        prt2D(self.solution)

    def prtMappedSolution(self):
        prt2D(self.mappedSolution)
    
    def prtDomain(self):
        prt3D(self.domain)

    def prtSolutions(self,count=None):
        if count==None or count>=len(self.solutions):
            count=len(self.solutions)
        for i in range(0,count):
            prt2D(self.solutions[i])

    def prtMappedSolutions(self,count=None):
        if count==None or count>=len(self.mappedSolutions):
            count=len(self.mappedSolutions)
        for i in range(0,count):
            prt2D(self.mappedSolutions[i])


