import numpy as np
def ewma(v,lam=.97):
    o=np.zeros(len(v))
    for t in range(1,len(v)): o[t]=lam*o[t-1]+(1-lam)*v[t]
    return o
def efmw_residual(v,lam=.97): return np.abs(ewma(v,lam))
def rolling_abs_mean(v,window=20):
    return np.array([abs(np.mean(v[max(0,t-window+1):t+1])) for t in range(len(v))])
def cusum_abs(v,k=.02):
    p=n=0.; o=np.zeros(len(v))
    for i,z in enumerate(v):
        p=max(0,p+z-k); n=max(0,n-z-k); o[i]=max(p,n)
    return o
def energy(x,b): return np.maximum(0,x*x-b)
def trajectory_ewma(x,b,lam=.97): return ewma(energy(x,b),lam)
def page_hinkley(v,delta=.005):
    mean=cum=minimum=0.; o=np.zeros(len(v))
    for i,z in enumerate(v,1):
        mean+=(z-mean)/i; cum+=z-mean-delta; minimum=min(minimum,cum); o[i-1]=cum-minimum
    return o
