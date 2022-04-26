from numpy import array
from csp import Csp
from support import *

class CspFutoshiki(Csp):
    def __init__(self, n,forwawrdChceck=True,filename=None):
        super().__init__(n,forwawrdChceck)
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
                #print("unique")
                return False
        return True
    
    def constraintLess(data,currId,id1,id2)->bool:
        #print(f"{data} {currId} {id1} {id2}")
        if(id1<=currId and id2<=currId and not data[id1]<data[id2]):
            #print(f"less {id1} {id2}")
            return False
        return True

    def valueSelected(self,x,y,value):
        if(self.forwawrdChceck):
            for i in range(x,self.n):
                for j in range(y,self.currY):
                    if(i!=x or j!=y):
                        self.constraintVariable[i,j].append(lambda val:value!=val)

    def valueUnSelected(self,x,y,value):
        if(self.forwawrdChceck):
            for i in range(x,self.n):
                for j in range(y,self.currY):
                    if(i!=x or j!=y):
                        self.constraintVariable[i,j].pop()

    def loadDomainFutoshiki(self,filename):
        start("load")
        defDom=[]
        for i in range(1,self.n+1):
            defDom.append(list(range(i,self.n+1))+list(range(1,i)))
        defDomId=0
        self.domain=[]
        for i in range(0,self.n):
            self.domain.append([])
            for _ in range(0,self.n):
                self.domain[i].append(defDom[defDomId])
                defDomId=(defDomId+1)%2
            defDomId=(defDomId+1)%2

        file=open(filename)
        for i in range(0,self.n):
            line=file.readline()
            for j in range(0,len(line)):
                if(line[j]=='x') or (line[j]=='-')or (line[j]=='\n'):
                    pass
                elif(line[j]=='<'):
                    #print(f"{i} {j} {(j>>1)+1} {j>>1}")
                    self.constraintRow[i].append(lambda data,currId,j=j:CspFutoshiki.constraintLess(data,currId,j>>1,(j>>1)+1))
                elif(line[j]=='>'):
                    #print(f"{i} {j} {(j>>1)+1} {j>>1}")
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
        stop("load")

    def setVariableQueue(self):
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
















