from random import randint

def ins(l):
    i,j,tmp=1,1,0
    while i<=(len(l)-1):
        j=i
        temp=l[j]
        while True:
            if j>0 and temp<l[j-1]:
                l[j]=l[j-1]
                j-=1
            else:
                l[j]=temp
                break
        i+=1

lista=[randint(0,1000) for x in range(randint(1,100))]
ins(lista)
if sorted(lista):
     print(True)
