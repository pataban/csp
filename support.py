import numpy as np
from pandas import DataFrame
import time

times=np.full((10,2),0.0)

def start(n):
    times[n,1]=time.time()

def stop(n):
    times[n,0]+=time.time()-times[n,1]

def prtTimes():
    print("times:")
    print(list(map(lambda i,t:f"{i}={round(t*1000)/1000}",range(0,9),times[:,0])))


def prt2D(data,size):
    columns=[]
    for i in range(0,size):
        columns.append(' ')
    index=[]
    for i in range(0,size):
        index.append(' ')
    #tupleDomain=map(lambda dom: (lambda d:tuple(d),dom),domain)
    print(DataFrame(data,columns=columns,index=index))

def prt3D(data):
    print(data)