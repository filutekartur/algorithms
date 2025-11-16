from random import randint
def qs(l,st,en):
    if (en-st)>0:
        piv=en
        i,j,=st-1,st
        tmp=0
        while j<piv:
                if l[j]<=l[piv]:
                    i+=1
                    tmp=l[j]
                    l[j]=l[i]
                    l[i]=tmp
                j+=1
        tmp=l[i+1]
        l[i+1]=l[piv]
        l[piv]=tmp 
        qs(l,st,i)#left
        qs(l,i+1,en)#right

lista=[randint(0,10000) for x in range(randint(1,100))]
qs(lista,0,len(lista)-1)
if sorted(lista):
     print(True)