import numpy as np

def randomization(n):
      if n>0 and n==int:
        A=np.random.random([n, 1])
    print(A)
x=int(input("enter a positive number: "))
r=randomization(x)
print(r)
    

def operations(h, w):
        A = np.random.randint(low=10, high=90, size=(h,w)) 
    
    
    B = np.random.randint(low=10, high=90, size=(h,w))
  
    
    s = A + B
    return A,B,s
    


def norm(A, B):
    
    s = A + B
    return np.linalg.norm(s)


def neural_network(inputs, weights):
        out = np.array(np.tanh(np.dot(weights.T, inputs)))
    return out

def scalar_function(x, y):
    if x <= y:
        return x*y
    else:
        return x/y
def vector_function(x, y):
    vec_function = np.vectorize(scalar_function)
    return vec_function(x, y)