#BS option pricing model
import numpy as np
from scipy import norm

def BS(r,S,K,T,sigma,type):
    d1= (np.log(S/K) + (sigma**2 + r)*T)/sigma*np.sqrt(T)
    d2=d1-sigma*np.sqrt(T)
    if type == "Call":
        return( S*norm.cdf(d1,0,1) - K*np.exp(-r*T)*norm.cdf(d2,0,1))
    elif type == "Put":
        return(K*np.exp(-r*T)*norm.cdf(-d2,0,1) - S*norm(-d1,0,1) )
    else:
        return("Enter Call or Put for the type")


r=0.01
S=30
K=40
T=240/365
sigma=0.3
print(BS(r,S,K,T,sigma,"Put"))