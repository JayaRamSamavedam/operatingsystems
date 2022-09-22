from collections import deque
q=deque()
#fifo page replace ment technique
psize=int(input("enter the size of the page table"))
ptable=[]
print("enter the pages")
a=(list(map(int,input().split())))
#assuming that list is empty
for i in range(len(a)):
    q.append(a[i])
    if(a[i] in ptable):
        q.remove(a[i])
    elif(a[i] not in ptable and len(ptable)<psize):
        ptable.append(a[i])
    elif(a[i] not in ptable):
        t = q.popleft()
        ptable[ptable.index(t)] = a[i]
    print(a[i],'->',ptable)