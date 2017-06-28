#Various helper functions for LazySPN

import numpy as np
from nodes import *

def partition(givenset, p, maxsize):
	l = list(givenset)
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

def randstruct(maxsize, scope, indsize, flag, sumcount=3, prodcount=3):
	if (flag==0):
		s = sumNode()
		arr = []
		for i in range(0,prodcount):
			s.children.append(randstruct(maxsize, scope, indsize, 1, sumcount, prodcount))
			arr.append(1)
		s.setwts(arr)
	if (flag==1):
		

