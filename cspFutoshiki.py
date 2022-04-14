from numpy import array
from csp import Csp
from support import *

class CspFutoshiki(Csp):
    def __init__(self, n,filename=None):
        super().__init__(n)
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


    def loadDomainFutoshiki(self,filename):
        start("load")
        self.domain=[]
        for i in range(0,self.n):
            self.domain.append([])
            for _ in range(0,self.n):
                self.domain[i].append(list(range(1,self.n+1)))

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

        















