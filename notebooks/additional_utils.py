# Copyright (C) 2018 Nicolas Tremblay.
# This file is part of the DPP4Coreset (Determinantal Point Processes for Coresets) toolbox
#
# The DPP4Coreset toolbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The DPP4Coreset toolbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# If you use this toolbox please kindly cite
#     N. Tremblay, S. Barthelmé, Pierre-Olivier Amblard.
#     Determinantal Point Processes for Coresets.
#     arxiv.org/pdf/1803.08700.pdf

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
    
    creates an Stochastic Block Model (SBM) graph with specified parameters:
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
    #    while Numedgesk > com_size[k]*(com_size[k]-1)/2:
    #        Numedgesk = np.random.binomial(com_size[k]*(com_size[k]-1)/2, pin, size=None)
        
        edges = np.array(random.sample(range(int(com_size[k]*(com_size[k]-1)/2)), Numedgesk))+1

        [Inew, Jnew] = ind2sub4up(edges);
        Inew = Inew - 1
        Jnew = Jnew - 1
        
        I = np.concatenate((I, Inew+com_size[:k].sum()), axis=0)
        J = np.concatenate((J, Jnew+com_size[:k].sum()), axis=0)
        
        
    for k in np.arange(q-1):
        Numedgesk = np.random.binomial(com_size[k]*(com_size[k+1:].sum()), pout, size=None)
        
#        aux_edges = np.random.permutation(int(com_size[k]*(com_size[k+1:].sum())))
#        edges = aux_edges[:Numedgesk]
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

def generate_concentric_circles(N_in, N_out, sigma_in, sigma_out):
    '''
    Create a simple data set made of two concentric distributions
    data, truth = generate_concentric_circles(N_in, N_out, sigma_in, sigma_out)
    '''
    data = np.empty((N_in+N_out,2)) * np.nan
    # first cluster
    x = 2*np.random.rand(1,N_out)-1;
    y = 2*np.random.rand(1,N_out)-1;
    data[:N_out,0] = x / np.sqrt(x**2 + y**2) + sigma_out * np.random.randn(1,N_out)
    data[:N_out,1] = y / np.sqrt(x**2 + y**2) + sigma_out * np.random.randn(1,N_out)

    # second cluster
    data[N_out:,0] = sigma_in * np.random.randn(1, N_in)
    data[N_out:,1] = sigma_in * np.random.randn(1, N_in)

    truth = np.zeros((N_in+N_out,))
    truth[N_out:]=1
    return data, truth