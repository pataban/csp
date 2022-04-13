import numpy as np
from pandas import DataFrame
import time

from sqlalchemy import values

times={}

def start(key):
    if not key in times:
        times[key]=[0.0,0.0]
    times[key][1]=time.time()

def stop(key):
    times[key][0]=time.time()-times[key][1]

def prtTimes():
    global times

    times=list(map(lambda k,v:(k,v[0]),times.keys(),times.values()))
    getT=lambda t:t[1]
    times.sort(key=getT,reverse=True)

    convertTime=lambda t:f"{t[0]} =".ljust(15)+f" {int(round(t[1]*1000))/1000}\n"
    times=map(convertTime,times)
    times=list(times)
    print("times:")
    print("".join(times))


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