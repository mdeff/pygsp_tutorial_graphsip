# The following functions are not in the pyGSP toolbox, but are useful for the notebooks presented here. Some of these functions will eventually appear in the box. They have not been thoroughly tested (especially the SBM code may be unstable at some moments). Also, sorry for the only few comments. Treat with care. Nicolas. 

import numpy as np
from scipy import sparse
import random
import collections 
from scipy import special 


def ind2sub4up(IND):
    ##IND2SUB4UP Subscripts from linear index for upper triangular matrix (only
    ##elements above diagonal)
    ##   IND2SUB4UP determines the equivalent subscript values corresponding to
    ##   a given single index into a 2D upper triangular matrix, excluded all
    ##   elements over the diagonal.
    
    J = np.round(np.floor(-.5 + .5 * np.sqrt(1 + 8 * (IND - 1))) + 2);
    I = np.round(J * (3 - J) / 2 + IND - 1);
    return I, J


def create_SBM(N,q,c,epsi,com_size):
    """  A, truth = create_SBM(N,q,c,epsi,com_size)
    
    creates a Stochastic Block Model (SBM) graph with specified parameters:
        - N nodes, 
        - q communites of sizes listed in com_size, 
        - an average degree of c,
        - and a difficulty \epsilon=epsi. 
    Outputs:
        - A the adjacency matrix of the SBM graph
        - truth, the ground truth of the underlying community structure. 
        
    Example of usage:
        N = 10000; # number of nodes
        q = 100; # number of communities
        c = 16; # average degree
        
        com_size = np.ones(q)*(N/q)
        com_size = com_size.astype(int)
        
        epsi_c=(c-np.sqrt(c))/(c+np.sqrt(c)*(q-1));#maximum difficulty
        epsi=epsi_c/4;# the closer to espi_c, the more difficult is the clust. task
        
        A, truth = create_SBM(N,q,c,epsi,com_size)
    """
    
    
    if com_size.sum() != N:
        raise ValueError("com_size.sum() != N")
        
    pin = (q*c)/(N-q+(q-1)*epsi*N)
    pout = (q*c*epsi)/(N-q+(q-1)*epsi*N)
    
    # first look at all intra-community links :
    I=np.array([]); J=np.array([]); truth=np.zeros(N);
    for k in np.arange(q): # for each community
        
        truth[com_size[:k].sum():com_size[:k+1].sum()] = k
        
        Numedgesk = np.random.binomial(com_size[k]*(com_size[k]-1)/2, pin, size=None) #draw from a binomial the total number of edges within community
        
        edges = np.array(random.sample(range(int(com_size[k]*(com_size[k]-1)/2)), Numedgesk))+1

        [Inew, Jnew] = ind2sub4up(edges);
        Inew = Inew - 1
        Jnew = Jnew - 1
        
        I = np.concatenate((I, Inew+com_size[:k].sum()), axis=0)
        J = np.concatenate((J, Jnew+com_size[:k].sum()), axis=0)
        
        
    for k in np.arange(q-1):
        Numedgesk = np.random.binomial(com_size[k]*(com_size[k+1:].sum()), pout, size=None)
        
        if Numedgesk != 0:
            edges = np.array(random.sample(range(int(com_size[k]*(com_size[k+1:].sum()))), Numedgesk))
        
            [Inew, Jnew] = np.unravel_index(edges, (com_size[k],com_size[k+1:].sum()))
        
            I = np.concatenate((I, Inew + com_size[:k].sum()), axis=0)
            J = np.concatenate((J, Jnew + com_size[:k+1].sum()), axis=0)
        
    data = np.ones(len(I))
    A=sparse.coo_matrix((data,(I,J)), shape=(N,N));
    A=A+A.T;
            
    return A, truth


def AR_index(c1,c2):
    """adjusted Rand - Hubert & Arabie 1985
    perf = AR_index(c1,c2)
    where c1 and c2 are two different community structures (vectors of same size) to be compared
    the index varies between -1 and 1 (1 is perfect match, -1 is perfect anti-match, 0 is expected if one of them is random)
    c1 and c2 must be vectors of integers
    """
    c1 = c1 - np.min(c1)
    c2 = c2 - np.min(c2)
    n = len(c1) # number cass  
    ng1 = np.max(c1) + 1
    ng2 = np.max(c2) + 1
        
    C = -np.ones((n,2))
    C[:,0] = c1
    C[:,1] = c2
    C = C.astype(int)
    
    d = collections.OrderedDict()
    for row in C:
        t = tuple(row)
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    
    confmat = np.zeros((ng1,ng2))
    for (key, value) in d.items():
        confmat[key[0], key[1]] = value
    
    confmat = confmat.astype(int)

    coltot = np.sum(confmat, axis=0)
    rowtot = np.sum(confmat.T, axis=0)

    nis = np.sum(rowtot ** 2)		#sum of squares of sums of rows
    njs = np.sum(coltot ** 2) 	    #sum of squares of sums of columns

    t1 = special.comb(n,2)            #total number of pairs of entities
    t2 = np.sum(np.sum(confmat**2))	#sum over rows & columnns of nij^2
    t3= .5 * (nis+njs)

    #Expected index (for adjustment)
    nc = (n * (n**2 + 1) - (n + 1) * nis - (n + 1) * njs + 2 * (nis * njs) / n) / (2 * (n - 1))

    A=t1+t2-t3		#no. agreements

    if t1==nc:
        res=0			#avoid division by zero; if k=1, define Rand = 0
    else:
        res = (A - nc) / (t1 - nc)		


    return res

def generate_concentric_circles(N_in, N_out, sigma_in, sigma_out, d=2):
    '''
    Create a simple data set made of two concentric distributions
    data, truth = generate_concentric_circles(N_in, N_out, sigma_in, sigma_out)
    '''
    data = np.empty((N_in+N_out,d)) * np.nan
    # first cluster
    x = 2*np.random.rand(N_out, d)-1
    x_sum = np.sqrt(np.sum(x**2,1))
    for dd in np.arange(d):
        data[:N_out,dd] = x[:,dd] / x_sum + sigma_out * np.random.randn(1,N_out)

    # second cluster
    data[N_out:, :] = sigma_in * np.random.randn(N_in, d)

    truth = np.zeros((N_in+N_out,))
    truth[N_out:]=1
    return data, truth

def get_approx_filter(c):
	filt_approx = lambda x: np.sum(np.tile(c[1:], (len(x), 1)) * np.cos(np.tile(np.arange(len(c)-1) + 1, (len(x), 1)) * np.transpose(np.tile(np.arccos(x), (len(c) - 1, 1)))), 1) + np.tile(c[0], (len(x), 1)).T * np.cos(0 * np.arccos(x)) / 2
	return filt_approx



