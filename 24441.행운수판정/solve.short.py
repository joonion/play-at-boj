L=list(range(1,10**6,2))
i=1
while i<len(L):k=L[i];del L[k-1::k];i+=1
s=set(L)
for n in [*open(0)][1:]:print("un"*(int(n)not in s)+"lucky")