
def euclidean_dist(x, y):
    if x==[] and y==[]:
        return "lengths must not be zero"
    elif len(x) > len(y) or len(x) < len(y):
        return "lengths must be equal"
    else:
        distancesum = 0
        
        for i in range(len(x)):
            distancesum += (x[i]-y[i])**2
            
        d = distancesum**(1/2)
        return d 

#test euclidean_dist([0,0], [1,0]) == 1
#print(euclidean_dist([0,0], [1,0])) 
#test euclidean_dist([0,0,0], [1,0,0]) == 1
#print(euclidean_dist([0,0,0], [1,0,0]))

def manhattan_dist(x, y):
    if x==[] and y==[]:
        return "lengths must not be zero"
    elif len(x) > len(y) or len(x) < len(y):
        return "lengths must be equal"
    else:
        d = 0
          
        for i in range(len(x)): 
            d += abs(x[i] - y[i])
                
        return d

#test manhattan_dist([0,0], [1,1]) = 2
#print(manhattan_dist([0,0], [1,1]))
#test sim.manhattan_dist([0,0,0], [1,1,1]) == 3
#print(manhattan_dist([0,0,0], [1,1,1]))

def jaccard_dist(x, y):
    if x==[] and y==[]:
        return "lengths must not be zero"
    else:
        intersection = len(list(set(x).intersection(y)))
        union = len(list(set(x).union(y)))
        d = 1 - float(intersection / union)
        return(d)

#test jaccard_dist([0,0], [1,0]) == .5
#print(jaccard_dist([0,0], [1,0]))
#test accard_dist([0,0,0], [1,1,1]) == 1
#print(jaccard_dist([0,0,0], [1,1,1]))

def cosine_sim(x, y):
    if x==[] and y==[]:
        return "lengths must not be zero"
    elif len(x) > len(y) or len(x) < len(y):
        return "lengths must be equal"
    else:
        sumxx=0; sumyy=0; sumxy=0;
        
        for i in range(len(x)):
            sumxx += x[i]*x[i]
            sumyy += y[i]*y[i]
            sumxy += x[i]*y[i]
        
        d = sumxy/(sumxx*sumyy)**(1/2)
        return(d)

#test cosine_sim([1,0], [1,0]) == 1
#print(cosine_sim([1,0], [1,0]))
#test cosine_sim([0,1,0], [1,0,0]) == 0
#print(cosine_sim([0,1,0], [1,0,0]))

# Feel free to add more
