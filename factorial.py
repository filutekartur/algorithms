def fac1(x):
    y=1
    if x>1:
        y=x*fac1(x-1)
    return y

print(fac1(5))