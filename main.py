from support import *
from cspBinary import CspBinary
from cspFutoshiki import CspFutoshiki

if __name__ == "__main__":
    csp1=None
    csp2=None
    csp3=None
    csp4=None
    data=9
    if data ==1:
        csp1=CspBinary(4,forwawrdChceck=False)
        csp2=CspBinary(4,forwawrdChceck=True)
        csp3=CspBinary(4,heuristics=False)
        csp4=CspBinary(4,heuristics=True)
    elif data==2:
        csp1=CspBinary(6,r"dane\binaryDemo",forwawrdChceck=False)
        csp2=CspBinary(6,r"dane\binaryDemo",forwawrdChceck=True)
        csp3=CspBinary(6,r"dane\binaryDemo",heuristics=False)
        csp4=CspBinary(6,r"dane\binaryDemo",heuristics=True)
    elif data==3:
        csp1=CspBinary(6,r"dane\binary_6x6",forwawrdChceck=False)
        csp2=CspBinary(6,r"dane\binary_6x6",forwawrdChceck=True)
        csp3=CspBinary(6,r"dane\binary_6x6",heuristics=False)
        csp4=CspBinary(6,r"dane\binary_6x6",heuristics=True)
    elif data==4:
        csp1=CspBinary(8,r"dane\binary_8x8",forwawrdChceck=False)
        csp2=CspBinary(8,r"dane\binary_8x8",forwawrdChceck=True)
        csp3=CspBinary(8,r"dane\binary_8x8",heuristics=False)
        csp4=CspBinary(8,r"dane\binary_8x8",heuristics=True)
    elif data==5:
        csp1=CspBinary(10,r"dane\binary_10x10",forwawrdChceck=False)
        csp2=CspBinary(10,r"dane\binary_10x10",forwawrdChceck=True)
        csp3=CspBinary(10,r"dane\binary_10x10",heuristics=False)
        csp4=CspBinary(10,r"dane\binary_10x10",heuristics=True)
    elif data==6:
        csp1=CspFutoshiki(4,r"dane\futoshikiDemo",forwawrdChceck=False)
        csp2=CspFutoshiki(4,r"dane\futoshikiDemo",forwawrdChceck=True)
        csp3=CspFutoshiki(4,r"dane\futoshikiDemo",heuristics=False)
        csp4=CspFutoshiki(4,r"dane\futoshikiDemo",heuristics=True)
    elif data==7:
        csp1=CspFutoshiki(4,r"dane\futoshiki_4x4",forwawrdChceck=False)
        csp2=CspFutoshiki(4,r"dane\futoshiki_4x4",forwawrdChceck=True)
        csp3=CspFutoshiki(4,r"dane\futoshiki_4x4",heuristics=False)
        csp4=CspFutoshiki(4,r"dane\futoshiki_4x4",heuristics=True)
    elif data==8:
        csp1=CspFutoshiki(5,r"dane\futoshiki_5x5",forwawrdChceck=False)
        csp2=CspFutoshiki(5,r"dane\futoshiki_5x5",forwawrdChceck=True)
        csp3=CspFutoshiki(5,r"dane\futoshiki_5x5",heuristics=False)
        csp4=CspFutoshiki(5,r"dane\futoshiki_5x5",heuristics=True)
    elif data==9:
        csp1=CspFutoshiki(6,r"dane\futoshiki_6x6",forwawrdChceck=False)
        csp2=CspFutoshiki(6,r"dane\futoshiki_6x6",forwawrdChceck=True)
        csp3=CspFutoshiki(6,r"dane\futoshiki_6x6",heuristics=False)
        csp4=CspFutoshiki(6,r"dane\futoshiki_6x6",heuristics=True)
    elif data==10:
        csp1=CspFutoshiki(7,r"dane\futoshiki_7x7",forwawrdChceck=False)
        csp2=CspFutoshiki(7,r"dane\futoshiki_7x7",forwawrdChceck=True)
        csp3=CspFutoshiki(7,r"dane\futoshiki_7x7",heuristics=False)
        csp4=CspFutoshiki(7,r"dane\futoshiki_7x7",heuristics=True)
    elif data==11:
        csp1=CspFutoshiki(7,r"dane\futoshiki_7x7_hard",forwawrdChceck=False)
        csp2=CspFutoshiki(7,r"dane\futoshiki_7x7_hard",forwawrdChceck=True)
        csp3=CspFutoshiki(7,r"dane\futoshiki_7x7_hard",heuristics=False)
        csp4=CspFutoshiki(7,r"dane\futoshiki_7x7_hard",heuristics=True)

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
    
    
