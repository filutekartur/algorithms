def fac1(x):
    if x>1:
        return x*fac1(x-1)
    else:
        return 1

print(fac1(5))