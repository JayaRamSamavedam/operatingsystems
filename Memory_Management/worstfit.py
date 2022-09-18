m=list(map(int,input().split()))
x=[i+1 for i in range(len(m))]
m=list(zip(x,m))
n=int(input())
a=[]
for i in range(n):
    f=int(input())
    a.append([i+1,f])

for i in range(len(m)):
    for j in range(0,len(m)-i-1):
        if(m[j][1] < m[j+1][1]):
            temp=m[j]
            m[j]=m[j+1]
            m[j+1]=temp

for i in range(len(a)):
    if(m[0][1]-a[i][1]>=0):
        a[i].append(m[0])
        m.remove(m[0])
    else:
        print("no sufficient memory")
for i in range(len(a)):
    print(a[i][0],"\t",a[i][1],"\t",a[i][2][0],"\t",a[i][2][1],"\t",a[i][2][1]-a[i][1])