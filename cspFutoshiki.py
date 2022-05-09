from numpy import array
from csp import Csp
from support import *

class CspFutoshiki(Csp):
    def __init__(self, n,filename=None,forwawrdChceck=True,heuristics=True):
        super().__init__(n,forwawrdChceck,heuristics)
        self.constraintRow=[]
        self.constraintCol=[]
        for _ in range(0,n):
            self.constraintRow.append([CspFutoshiki.constraintUnique])
            self.constraintCol.append([CspFutoshiki.constraintUnique])
        self.constraintGlobal=[]
        
        if filename is None:
            self.setDomain(list(range(1,self.n+1)))
        else:
            self.loadDomainFutoshiki(filename)

        self.setVariableQueue()

    
    def constraintUnique(data,currId)->bool:
        count=np.full_like(data,0)
        for d in data[:currId+1]:
            count[d-1]+=1
        for c in count:
            if c>1:
                return False
        return True
    
    def constraintLess(data,currId,id1,id2)->bool:
        if(id1<=currId and id2<=currId and not data[id1]<data[id2]):
            return False
        return True

    def valueSelected(self,x,y,value):
        if(self.forwawrdChceck):
            for i in range(x+1,self.n):
                self.constraintVariable[i,y].append(lambda val,value=value:value!=val)
            for j in range(y+1,self.n):
                self.constraintVariable[x,j].append(lambda val,value=value:value!=val)

    def valueUnSelected(self,x,y,value):
        if(self.forwawrdChceck):
            for i in range(x+1,self.n):
                self.constraintVariable[i,y].pop()
            for j in range(y+1,self.n):
                self.constraintVariable[x,j].pop()

    def loadDomainFutoshiki(self,filename):
        defDomId=0
        defDom=[list(range(1,self.n+1))]
        if self.heuristics:
            for i in range(2,self.n+1):
                defDom.append(list(range(i,self.n+1))+list(range(1,i)))
        self.domain=[]
        for i in range(0,self.n):
            self.domain.append([])
            for _ in range(0,self.n):
                self.domain[i].append(defDom[defDomId])
                defDomId=(defDomId+1)%len(defDom)
            defDomId=(defDomId+1)%len(defDom)

        file=open(filename)
        for i in range(0,self.n):
            line=file.readline()
            for j in range(0,len(line)):
                if(line[j]=='x') or (line[j]=='-')or (line[j]=='\n'):
                    pass
                elif(line[j]=='<'):
                    self.constraintRow[i].append(lambda data,currId,j=j:CspFutoshiki.constraintLess(data,currId,j>>1,(j>>1)+1))
                elif(line[j]=='>'):
                    self.constraintRow[i].append(lambda data,currId,j=j:CspFutoshiki.constraintLess(data,currId,(j>>1)+1,j>>1))
                else:
                    self.domain[i][j>>1]=[int(line[j])]
            if i+1<=self.n:
                line=file.readline()
                for j in range(0,len(line)):
                    if(line[j]=='<'):
                        self.constraintCol[j].append(lambda data,currId,i=i:CspFutoshiki.constraintLess(data,currId,i,i+1))
                    elif(line[j]=='>'):
                        self.constraintCol[j].append(lambda data,currId,i=i:CspFutoshiki.constraintLess(data,currId,i+1,i))
        
        self.domain=np.array(self.domain,dtype=list)
        self.mapSolution()

    def setVariableQueue(self):
        if self.heuristics:
            for i in range(0,self.n):
                for j in range(0,self.n):
                    if(len(self.domain[i,j])==1):
                        self.currV+=1
                        self.variableQueue[self.currV]=(i,j)
                        
        
        varQId=self.currV+1
        for i in range(0,self.n):
            for j in range(0,self.n):
                if not self.heuristics or (len(self.domain[i,j])!=1):
                    self.variableQueue[varQId]=(i,j)
                    varQId+=1
















