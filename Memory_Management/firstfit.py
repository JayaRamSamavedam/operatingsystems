m=list(map(int,input().split()))
x=[i+1  for i in range(len(m))]
m=list(zip(x,m))
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append([i+1,x])

def find(n,a):
    for i in range(len(a)):
        if(a[i][1]-n >=0):
            return a[i]

for i in range(len(a)):
    x=find(a[i][1],m)
    a[i].append(x)
    m.remove(x)

for i in range(len(a)):
    print(a[i][0],"\t",a[i][1],"\t",a[i][2][0],"\t",a[i][2][1],"\t",a[i][2][1]-a[i][1])