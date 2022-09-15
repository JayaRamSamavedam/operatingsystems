import operator


def func(a,b,x):
    j=0
    for i in range(x,-1,-1):
        if(b[i]==a):
            return i
    return -1
# a is the element
#b is the list
# we have to find the index which is having the highest distance
psize=int(input("enter the size of the page table"))
ptable=[]
print("enter the pages")
a=(list(map(int,input().split())))
for i in range(len(a)):
    if(a[i] not in ptable):
        if(len(ptable)<psize):
            ptable.append(a[i])
        else:
            d={ptable[h]:func(ptable[h],a,i-1) for h in range(len(ptable))}
            print(d)
            d=dict(sorted(d.items(), key=operator.itemgetter(1)))
            c=list(d.items())
            ptable[ptable.index(c[0][0])]=a[i]
    print(ptable)


