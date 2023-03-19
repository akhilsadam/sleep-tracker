from itertools import cycle, islice

# coerce lists
def coercion(L1,L2):
    len1 = len(L1)
    len2 = len(L2)
    llen = max(len1,len2)
    
    if(llen==len1):
        L2 = list(islice(cycle(L2), llen))
    else: L1 = list(islice(cycle(L1), llen))  
        
    return (L1,L2,llen)

# join filepath lists
def join(L1,L2): 
    L1,L2,llen = coercion(L1,L2)

    L3 = [(L1[i]+L2[i]) for i in range(llen)]
    return L3

def tuplejoin(L1,L2,L3): 
    L1,L2,llen = coercion(L1,L2)
    L2,L3,llen = coercion(L2,L3)
    
    L4 = [(L1[i],L2[i],L3[i]) for i in range(llen)]
    return L4

# subtract strings (actually character arrays)
def subtract(S1,S2):
    return S1.replace(S2,'')
