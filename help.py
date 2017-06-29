#Various helper functions for LazySPN

import numpy as np
from nodes import *

def partition(givenset, p, maxsize):
	l = list(givenset)
	l = np.random.permutation(l)
	tot = len(l)
	eff = 10*p-0.5
	returnlist = []
	init = 0
	for i in range(0, tot):
		rand = np.random.randint(0,10)
		if (i==(tot-1)):
			returnlist.append(set(l[init:tot]))
			break
		if ((i-init)>=maxsize-1):
			returnlist.append(set(l[init:i+1]))
			init = i+1
			continue		
		if (rand>eff):
			returnlist.append(set(l[init:i+1]))
			init = i+1
	return(returnlist)

#test

s = set(xrange(10))

print(partition(s,0.4,3))

print(np.random.rand(7,1))	


def gauss(nvar):
	mean = np.random.rand(nvar,1)
	sampler = np.random.rand(nvar,10)
	temp = np.transpose(sampler)
	cov = 0.01*np.matmul(sampler,temp)
	return mean, cov

x,y = gauss(10)

print(x)
print(np.shape(y))
print(y)
	

def randstruct(maxsize, scope, indsize, flag, sumcount=3, prodcount=3):
	if (flag==0):
		s = sumNode()
		arr = []
		for i in range(0,prodcount):
			s.children.append(randstruct(maxsize, scope, indsize, 1, sumcount, prodcount))
			arr.append(1)
		s.setwts(arr)
		return s
	if (flag==1):
		if(len(scope)<=(indsize)):
			l = leafNode()
			l.scope = scope			
			tempmean,tempcov = gauss(len(scope))
			l.create(tempmean,tempcov)
			return l	
		else:
			p = prodNode()
			setlist = partition(scope, 0.5, maxsize)
			j = 0
			for i in range(0,len(setlist)):
				p.children.append(randstruct(maxsize-1,setlist[j],indsize,0,sumcount,prodcount))
				j = j+1
			return p
			
			

ab = np.genfromtxt('../AB.dat',delimiter=",")
ab = np.asarray(ab[:,1:])

s = set(xrange(8))

Tst = randstruct(6,s,4,0)	

print(Tst)	

