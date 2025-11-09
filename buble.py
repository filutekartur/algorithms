from random import randint

lista= [randint(0,100) for x in range(randint(2,20))]
loops,changes = 0,0
change=True
print(f"Lista wejściowa: {lista}")
while change:
    change=False
    j=1
    while j<len(lista):
        if lista[j-1]>lista[j]:
            temp=lista[j-1]
            lista[j-1]=lista[j]
            lista[j]=temp
            changes+=1
            change=True
        j+=1
    loops+=1
print(f"Lista wyjściowa: {lista}")
print(f"Pętla wykonałą się {loops} razy.")
print(f"Zamieniono {changes} pozycji.")