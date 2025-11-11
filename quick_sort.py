lista1=[3,1,2]
lista2=[3,1,2,5]
lista3=[3,1,2,5,7,0]
lista=lista2
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

# temp=lista[index1-1]
# lista[index1-1]=lista[pivot]
# lista[pivot]=temp

print(lista)