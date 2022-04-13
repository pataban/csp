from support import *
from cspBinary import CspBinary
from cspFutoshiki import CspFutoshiki

if __name__ == "__main__":
    csp=None
    data=1
    if data ==1:
        csp=CspBinary(4)
    elif data==2:
        csp=CspBinary(6,r"dane\binaryDemo")
    elif data==3:
        csp=CspBinary(6,r"dane\binary_6x6")
    
    #csp.prtDomain()
    #csp.prtSolution()

    csp.getFirst()
    
    print(f"count={csp.solutionCount}")
    csp.prtMappedSolutions(1)
    
    prtTimes()

    #csp2=Csp(4,list(range(1,5)),r'dane\futoshiki_4x4', 'futoshiki')
    #csp2.prtDomain()
    
