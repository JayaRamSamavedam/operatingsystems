n=int(input("enter the number of processes"))
b=[]
for i  in range(n):
    #it take a list of value such as pid  arrival time burst time
    #a[1]=arrival time
    #a[2]=burst time
    #a[3]=starting time
    #a[4]=exit time
    #a[5]=turn arround time
    #a[6]=
    a=list(map(int,input().split()))
    b.append(a)
for i in range(len(b)):
    for j in range(0,len(b)-i-1):
        if(b[j][1]>b[j+1][1]):
            temp=b[j]
            b[j]=b[j+1]
            b[j+1]=temp
for i in range(n):
    pid=b[i][0]
    at=b[i][1]
    bt=b[i][2]
    if(i==0):
        st=0
        et=st+bt
        tat=et-at
        wt=tat-bt
        b[i].append(st)
        b[i].append(et)
        b[i].append(tat)
        b[i].append(wt)
    else:
        if(b[i-1][4]<b[i][1]):
            st=at#st=at
        else:
            st=b[i-1][4]
        et=st+bt
        tat=et-at
        wt=tat-bt
        b[i].append(st)
        b[i].append(et)
        b[i].append(tat)
        b[i].append(wt)
for i in range(len(b)):
    for j in range(0,len(b)-i-1):
        if(b[j][0]>b[j+1][0]):
            temp=b[j]
            b[j]=b[j+1]
            b[j+1]=temp
print("pid\tat \tbt \tst \tet \ttat\twt")
for i in b:
    for j in range(len(i)):
        print(i[j],end='\t')
    print()
