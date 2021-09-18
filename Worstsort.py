def lexOrder(L1,L2):
	if type(L1)==int:return L1-L2
	i=0
	while L1[i]==L2[i]:
		i+=1
		if i==len(L1):return 0
	return lexOrder(L1[i],L2[i])

def bubblesort(L):
	for i in range(len(L)):
		for j in range(len(L)-1-i):
			if lexOrder(L[j],L[j+1])>0:
				L[j],L[j+1]=L[j+1],L[j]
	return L

def permutations(L):
	if L==[]:return[L]
	mix=[]
	for i in range(len(L)):
		for sub in permutations(L[:i]+L[i+1:]):
			mix+=[[L[i]]+sub]
	return mix

def p(L):
	if L:return[[L[i]]+s for i in range(len(L))for s in p(L[:i]+L[i+1:])]
	return[L]

def badsort(L,k):
	if k==0:return bubblesort(L)
	return badsort(permutations(L),k-1)[0]

def f(n):
	import Googology
	return Googology.BH(n)

def worstsort(L,f):return badsort(L,f(len(L)))
