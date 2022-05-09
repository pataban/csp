from support import *
from cspBinary import CspBinary
from cspFutoshiki import CspFutoshiki


dataBinary=[  
    (4,None),
    (6,r"dane\binaryDemo"),
    (6,r"dane\binary_6x6"),
    (8,r"dane\binary_8x8"),
    (10,r"dane\binary_10x10")
]

dataFutoshiki=[  
    (4,r"dane\futoshikiDemo"),
    (4,r"dane\futoshiki_4x4"),
    (5,r"dane\futoshiki_5x5"),
    (6,r"dane\futoshiki_6x6"),    
    (7,r"dane\futoshiki_7x7"),
    (7,r"dane\futoshiki_7x7_hard")
]

if __name__ == "__main__":
    #0 - binary or 1 - futoshiki
    cspType=1
    dataId=2
    
    csp1=None
    csp2=None
    csp3=None
    csp4=None
    
    if cspType==0:
        csp1=CspBinary(dataBinary[dataId][0],dataBinary[dataId][1],forwawrdChceck=False)
        csp2=CspBinary(dataBinary[dataId][0],dataBinary[dataId][1],forwawrdChceck=True)
        csp3=CspBinary(dataBinary[dataId][0],dataBinary[dataId][1],heuristics=False)
        csp4=CspBinary(dataBinary[dataId][0],dataBinary[dataId][1],heuristics=True)
    elif cspType==1:
        csp1=CspFutoshiki(dataFutoshiki[dataId][0],dataFutoshiki[dataId][1],forwawrdChceck=False)
        csp2=CspFutoshiki(dataFutoshiki[dataId][0],dataFutoshiki[dataId][1],forwawrdChceck=True)
        csp3=CspFutoshiki(dataFutoshiki[dataId][0],dataFutoshiki[dataId][1],heuristics=False)
        csp4=CspFutoshiki(dataFutoshiki[dataId][0],dataFutoshiki[dataId][1],heuristics=True)
        

    print("backTracking:")
    csp1.getFirst()
    csp1.prtMappedSolutions(1)
    prtNodes()
    prtTimes()

    clrNodes()
    clrTimes()

    print("forwardChecking:")
    csp2.getFirst()
    csp2.prtMappedSolutions(1)
    prtNodes()
    prtTimes()

    clrNodes()
    clrTimes()

    print("no Heuristics:")
    csp3.getFirst()
    csp3.prtMappedSolutions(1)
    prtNodes()
    prtTimes()

    clrNodes()
    clrTimes()

    print("Heuristics:")
    csp4.getFirst()
    csp4.prtMappedSolutions(1)
    prtNodes()
    prtTimes()
    
    
