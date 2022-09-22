
#it will find the nearest nukber in the given array
def find(n,d):
    a=[(d[i],abs(n-d[i])) for i in range(len(d)) if(d[i]!=n)]
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if(a[j][1]>a[j+1][1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a[0][0]
a=list(map(int,input().split()))
n=int(input("enter the start"))
f=find(n,a)
d=abs(n-f)
a.remove(f)
for i in range(len(a)):
    x=find(f,a)
    d+=abs(f-x)
    f=x
    a.remove(f)
print("difference:",d)