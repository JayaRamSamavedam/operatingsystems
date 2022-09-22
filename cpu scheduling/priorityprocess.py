#sjf
"""case 1:
int first case we have to check the process have least aarrival time
if many process are coming at same time we have to check for the burst time"""
def sortat(bt,p):
    a=[]
    for i in range(len(p)):
        if(p[i][1]<=bt):
            a.append(p[i])
    return a

def sortpt(a):
    for i in range(len(a)):
        for j in range(0,len(a)-1-i):
            if(a[j][3] > a[j+1][3]):
                a[j],a[j+1]=a[j+1],a[j]
            elif(a[j][3]==a[j+1][3]):
                if(a[j][1]>a[j+1][1]):
                    a[j],a[j+1]=a[j+1],a[j]
#read the number of process
n=int(input())
#read the process information into a list
#in the form of pid , at ,bt - > pid->0,at->1,bt->2

p=[]

for i in range(n):
    t=list(map(int,input().split()))
    p.append(t)
#we take a variable to maintain current time
#initial arrival time is the burst time
#first we will sort the process according to burst time

for i in range(len(p)):
    for j in range(0,len(p)-i-1):
        if(p[j][1]>p[j+1][1]):
            temp=p[j]
            p[j]=p[j+1]
            p[j+1]=temp

#it will sort the process acording to their arrival time
#now we will take the least arrival times burts time
# we take a variable named as cbt
#we take a object named fp to store the values
cbt=0
a=[p[i] for i in range(len(p)) if(p[0][1] == p[i][1])]

for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j+1][2] < a[j][2]):
            temp=a[j+1]
            a[j+1]=a[j]
            a[j]=temp

#from this we will get the least arrival time with least burst time

#process will have another list we will append it into that list

process=[]
process.append(a[0])

p.pop(p.index(a[0]))

cbt=process[0][2]

for i in range(len(p)):
    a=sortat(cbt,p)
    sortpt(a)
    cbt+=a[0][2]
    process.append(a[0])
    p.pop(p.index(a[0]))
print(process)
b=process
for i in range(n):
    pid=b[i][0]
    at=b[i][1]
    bt=b[i][2]
    if(i==0):
        st=at
        et=st+bt
        tat=et-at
        wt=tat-bt
        b[i].append(st)
        b[i].append(et)
        b[i].append(tat)
        b[i].append(wt)
    else:
        if(b[i-1][5]<b[i][1]):
            st=at#st=at
        else:
            st=b[i-1][5]
        et=st+bt
        tat=et-at
        wt=tat-bt
        b[i].append(st)
        b[i].append(et)
        b[i].append(tat)
        b[i].append(wt)
print("pid\tat \tbt \tpt \tst \tet \ttat\twt")

for i in range(len(b)):
    for j in range(0,len(b)-i-1):
        if(b[j+1][0] < b[j][0]):
            temp=b[j+1]
            b[j+1]=b[j]
            b[j]=temp

for i in b:
    for j in range(len(i)):
        print(i[j],end='\t')
    print()
