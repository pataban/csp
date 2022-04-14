from support import *
from cspBinary import CspBinary
from cspFutoshiki import CspFutoshiki

if __name__ == "__main__":
    csp=None
    data=9
    if data ==1:
        csp=CspBinary(4)
    elif data==2:
        csp=CspBinary(6,r"dane\binaryDemo")
    elif data==3:
        csp=CspBinary(6,r"dane\binary_6x6")
    elif data==4:
        csp=CspBinary(8,r"dane\binary_8x8")
    elif data==5:
        csp=CspBinary(10,r"dane\binary_10x10")
    elif data==6:
        csp=CspFutoshiki(4,r"dane\futoshikiDemo")
    elif data==7:
        csp=CspFutoshiki(4,r"dane\futoshiki_4x4")
    elif data==8:
        csp=CspFutoshiki(5,r"dane\futoshiki_5x5")
    elif data==9:
        csp=CspFutoshiki(6,r"dane\futoshiki_6x6")



    print(f"result = {csp.getFirst()}")
    csp.prtMappedSolutions(1)
    prtTimes()

    
    
