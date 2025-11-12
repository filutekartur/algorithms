def qs(l,st,en):
    if len(l)>1:
        piv=en
        i,j,tmp=st-1,st,0
        while j<pivot:
                if l[j]<l[piv]:
                    i+=1
                    tmp=l[j]
                    l[j]=l[i]
                    l[i]=tmp
                j+=1
        tmp=l[i+1]
        l[i+1]=l[piv]
        l[piv]=tmp
    return l    



lista1=[7,5,3,1,6,2,4]
lista2=[3,1,2,5]
lista3=[3,1,2,5,7,0]
lista=lista1
listaa=[7,5,3,1,6,2,4]
print(lista)
pivot=len(lista)-1
index0=-1
index1=0
temp=0

while index1<pivot:
    if lista[index1]<lista[pivot]:
        index0+=1
        temp=lista[index1]
        lista[index1]=lista[index0]
        lista[index0]=temp
    index1+=1
print(lista)
print(index0,index1)

temp=lista[index0+1]
lista[index0+1]=lista[pivot]
lista[pivot]=temp

# temp=lista[index1-1]
# lista[index1-1]=lista[pivot]
# lista[pivot]=temp

print(lista)
print(index0,index1)
