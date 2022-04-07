from support import *
from cspBinary import CspBinary
from cspFutoshiki import CspFutoshiki

if __name__ == "__main__":
    #csp=CspBinary(6,r"dane\binary_6x6")
    #csp=CspBinary(6,r"dane\binaryDemo")
    csp=CspBinary(4)
    #csp.prtDomain()
    #csp.prtSolution()

    csp.getFirst()
    
    print(f"count={csp.solutionCount}")
    csp.prtMappedSolutions(1)
    
    prtTimes()

    #csp2=Csp(4,list(range(1,5)),r'dane\futoshiki_4x4', 'futoshiki')
    #csp2.prtDomain()
    
