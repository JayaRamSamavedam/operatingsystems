#least recently used

from  collections import deque
stack=deque()
psize=int(input("enter the size of the page table"))
ptable=[]
print("enter the pages")
a=(list(map(int,input().split())))

for i in range(len(a)):

    if (a[i] in ptable):
        stack.remove(a[i])
    stack.append(a[i])
    if (a[i] not in ptable and len(ptable) < psize):
        ptable.append(a[i])
    elif (a[i] not in ptable):
        t = stack.popleft()
        ptable[ptable.index(t)] = a[i]
    print(a[i], '->', ptable)
