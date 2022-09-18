a=list(map(int,input().split()))
n=int(input("enter the start"))
d=abs(n-a[0])
for i in range(1,len(a)):
    d+=abs(a[i-1]-a[i])
print(d)