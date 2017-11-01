import random

def check(arr):
	zerocount=0
	for i in arr:
		if (i==0):
			zerocount+=1
			if (zerocount==len(arr)):
				return 1
		if (i<0):
			return -1
		else:
			return 0

def isGraphic(degseq):
	#degseq=sorted(degseq, key=int, reverse=True)
	newdegseq=[]
	if (check(degseq)==0):
		del degseq[0]
		for vertex in degseq:
			degseq[vertex]-=1
			newdegseq[vertex]=degseq[vertex]
		return isGraphic(newdegseq)
	if (check(newdegseq)==1):
		print "graphic sequence"
	if (check(newdegseq==-1)):
		print "not a graphic sequence"

def fill(n):
	l=[]
	l.extend(range(1, n))
	return l


isGraphic(fill(5))



