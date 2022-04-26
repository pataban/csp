from support import *
from cspBinary import CspBinary
from cspFutoshiki import CspFutoshiki

if __name__ == "__main__":
    csp1=None
    csp2=None
    data=8
    if data ==1:
        csp1=CspBinary(4,False)
        csp2=CspBinary(4,True)
    elif data==2:
        csp1=CspBinary(6,False,r"dane\binaryDemo")
        csp2=CspBinary(6,True,r"dane\binaryDemo")
    elif data==3:
        csp1=CspBinary(6,False,r"dane\binary_6x6")
        csp2=CspBinary(6,True,r"dane\binary_6x6")
    elif data==4:
        csp1=CspBinary(8,False,r"dane\binary_8x8")
        csp2=CspBinary(8,True,r"dane\binary_8x8")
    elif data==5:
        csp1=CspBinary(10,False,r"dane\binary_10x10")
        csp2=CspBinary(10,True,r"dane\binary_10x10")
    elif data==6:
        csp1=CspFutoshiki(4,False,r"dane\futoshikiDemo")
        csp2=CspFutoshiki(4,True,r"dane\futoshikiDemo")
    elif data==7:
        csp1=CspFutoshiki(4,False,r"dane\futoshiki_4x4")
        csp2=CspFutoshiki(4,True,r"dane\futoshiki_4x4")
    elif data==8:
        csp1=CspFutoshiki(5,False,r"dane\futoshiki_5x5")
        csp2=CspFutoshiki(5,True,r"dane\futoshiki_5x5")
    elif data==9:
        csp1=CspFutoshiki(6,False,r"dane\futoshiki_6x6")
        csp2=CspFutoshiki(6,True,r"dane\futoshiki_6x6")
    elif data==10:
        csp1=CspFutoshiki(7,False,r"dane\futoshiki_7x7")
        csp2=CspFutoshiki(7,True,r"dane\futoshiki_7x7")
    elif data==11:
        csp1=CspFutoshiki(7,False,r"dane\futoshiki_7x7_hard")
        csp2=CspFutoshiki(7,True,r"dane\futoshiki_7x7_hard")

    print("backTracking:")
    print(f"result = {csp1.getFirst()}")
    csp1.prtMappedSolutions(1)
    prtTimes()

    clrTimes()

    print("forwardChecking:")
    print(f"result = {csp2.getFirst()}")
    csp2.prtMappedSolutions(1)
    prtTimes()
    
