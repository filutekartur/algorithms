from random import randint

lista1=[randint(0,10000) for x in range(randint(1,100))]
lista2=[3,2,1]
lista=lista2

def ins(l):
    i,j,tmp=1,1,0
    en=len(l)-1
    while i<=en:
        j=i
        temp=l[j]
        while temp<l[j-1]:
            l[j]=l[j-1]
            j-=1
        i+=1