f={}
f['root']=[]
a=True
while(a):
    print("\n1.New File\n2.Display files\n3.Exit")
    n=int(input())
    if(n==1):
        print("enter root to save in root folder and root/directoryname")
        x=input().split('/')
        if(len(x)==2):
            f[x[1]]=[]
            f[x[1]].append(input("enter the file name"))
        else:
            f['root'].append(input("enter the file name"))
    elif(n == 2):
        x=list(zip(f.keys(),f.values()))
        for i in x:
            print(i[0],":")
            for f in range(1,len(i)):
                print(i[f][0])
    else:
        a=False
