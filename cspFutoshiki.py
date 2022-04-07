from csp import Csp


class CspFutoshiki(Csp):
    pass







def loadDomainFutoshiki(self,filename=None):
        if filename==None:
            return
        file=open(filename)     #load ograniczenia
        for i in range(0,self.n):
            line=file.readline()
            for j in range(0,len(line)):
                if(line[j]=='1'):
                    self.domain[i][int(j/2)]=[1]
                elif(line[j]=='2'):
                    self.domain[i][int(j/2)]=[2]
                elif(line[j]=='3'):
                    self.domain[i][int(j/2)]=[3]
                elif(line[j]=='4'):
                    self.domain[i][int(j/2)]=[4]

            line=file.readline()




















