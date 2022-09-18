a=list(map(int,input().split()))
start=int(input())
end=int(input())
ast=[a[i] for i in range(len(a)) if a[i]<start]
aend=[a[i] for i in range(len(a)) if a[i] not in ast]
ast.sort(reverse=True)
aend.sort(reverse=True)
ast.append(0)
ast.append(end)
for i in range(len(aend)):
    ast.append(aend[i])
d=abs(start-ast[0])
for i in range(1,len(ast)):
    if(ast[i]!=end):
        d+=abs(ast[i-1]-ast[i])
print(d)