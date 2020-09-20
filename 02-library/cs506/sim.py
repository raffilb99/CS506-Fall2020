
import math

def euclidean_dist(x, y):
    sum = 0
    for value in x:
        sum += ((value - y[value]) ** 2)
    return (sum ** (0.5))
        
    #raise NotImplementedError()

def manhattan_dist(x, y):
    sum = 0
    for value in x:
        sum += ((value - y[value]) ** 1)
    return (sum ** (1))
    #raise NotImplementedError()

def jaccard_dist(x, y):
    union = 0
    for values1 in x:
        union += values1
    for values2 in y:
        union += values2
        
    intersection = 0
    for values3 in x:
        if values3 in y:
            intersection += values3
    return (1 - (intersection/union))
        
            
        
    #raise NotImplementedError()
    

def cosine_sim(x, y):
    pq = 0
    for value1 in x:
        pq += (x[value1] * y[value1])
    p = 0
    for value2 in x:
        p += value2 * value2
    p = math.sqrt(p)
    q = 0
    for value3 in y:
        q += value3 * value3
    q = math.sqrt(q)
    bottom = p*q
    return (pq/bottom)
