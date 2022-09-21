a=True
f=[]
while(a):
    print("\n1.New File\n2.Display files\n3.Exit")
    n=int(input())
    if(n==1):
        x=str(input())
        f.append(x)
    elif(n==2):
        for x in f:
            print(x,end=' ')
    else:
        a=False
