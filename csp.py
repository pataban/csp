from pandas import DataFrame
import copy
import numpy as np
import time
from support import *

class Csp():
    def __init__(self, n):
        self.n=n
        self.domain=None
        self.solution=np.full((n,n),0)
        self.solutions=[]
        self.solutionCount=0
        self.currX=0
        self.currY=-1
        self.constraintRow=[]
        self.constraintCol=[]
        self.constraintGlobal=[]
            
    def setDomain(self,domain):
        self.domain=[]
        for i in range(0,self.n):
            self.domain.append([])
            for j in range(0,self.n):
                self.domain[i].append(domain)
        self.domain=np.array(self.domain)
  
    def mapSolution(self,solution):
        start(2)
        data=np.array(solution)
        """for i in range(0,solution.shape[0]):
            for j in range(0,solution.shape[1]):
                #if solution[i][j] is not None:
                data[i][j]=self.domain[i,j,solution[i][j]]"""
        for i,(dom, sol) in enumerate(zip(self.domain,self.solution)):  #jakims cudem to jest wolniejsze chyba
            for j,(d,s) in enumerate(zip(dom,sol)):
                data[i,j]=d[s]
                
        #data=np.array(list(map(lambda sol,dom:list(map(lambda s,d:None if(s==None) else d[s],sol,dom)),solution,self.domain)))
        stop(2)
        return data


    def chkConstraints(self)->bool:
        mappedSolution=self.mapSolution(self.solution)
        start(3)
        
        start(6)
        for conR,mSol in zip(self.constraintRow,mappedSolution):
            if(not conR(mSol)):
                stop(3)
                stop(6)
                return False

        for i, conC in enumerate(self.constraintCol):
            if(not conC(mappedSolution[:,i])):
                stop(3)
                stop(6)
                return False
        stop(6)
        
        start(5)
        for conG in self.constraintGlobal:
            if(not conG(mappedSolution)):
                stop(3)
                stop(5)
                return False
        stop(5)
        
        stop(3)
        return True

    def chkSolution(self):
        return ((self.currX+1==self.n) and (self.currY+1==self.n))

    def saveSolution(self):
        start(7)
        self.solutionCount+=1
        self.solutions.append(copy.deepcopy(self.solution))
        #self.prtSolution()
        stop(7)

  
    def nextSolution(self)->bool:   #false on finished all
        start(1)
        if((self.currX+1==self.n) and (self.currY+1==self.n)):  #full
            stop(1)
            return self.backTrack()
        while not ((self.currX+1==self.n) and (self.currY+1==self.n)):
            self.currY+=1
            if(self.currY>=self.n):
                self.currY=0
                self.currX+=1
            self.solution[self.currX][self.currY]=0
        stop(1)
        return True        

    def backTrack(self)-> bool: #false on finished all
        start(4)
        while(self.solution[self.currX][self.currY]+1>=self.domain.shape[2]):
            if(self.currY>0):
                self.currY-=1
            elif(self.currX>0):
                self.currY=self.n-1
                self.currX-=1
            else:
                stop(4)
                return False
        self.solution[self.currX][self.currY]+=1
        stop(4)
        return True

    def getFirst(self)->bool:
        start(0)
        while(self.nextSolution()):
            if(self.chkConstraints()):
                self.saveSolution()
                stop(0)
                return True
        stop(0)
        return False

    def getAll(self)->bool:
        found=False
        while(self.getFirst()):
            found=True
        return found
    
    def prtSolution(self):
        prt2D(self.solution,self.n)

    def prtMappedSolution(self):
        prt2D(self.mapSolution(self.solution),self.n)
    
    def prtDomain(self):
        prt3D(self.domain)

    def prtSolutions(self,count=None):
        if count==None or count>=len(self.solutions):
            count=len(self.solutions)
        for i in range(0,count):
            prt2D(self.solutions[i],self.n)

    def prtMappedSolutions(self,count=None):
        if count==None or count>=len(self.solutions):
            count=len(self.solutions)
        for i in range(0,count):
            prt2D(self.mapSolution(self.solutions[i]),self.n)


