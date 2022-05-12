dnum=int(input('enter the decimal number:'))
i=0
bnum=[]
while dnum!=0:
    rem=dnum%2
    bnum.append(rem)
    i=i+1
    dnum=dnum//2
i=i-1
print('\nEquivalent Binary Value is :',end=' ')
while i>=0:
    print(end=str(bnum[i]))
    i=i-1
print()
