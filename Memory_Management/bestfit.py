"""bestfit algorithm"""
"""in best fit algorithm we take the array of the memory holes and we take the number of the memory to be allocated to number of the process 
then in best fit we sort it we allocate the exact or the smallest memory which ful fill the requirements
suppsose if there is the least hole with 5 but we need 4 it allocate the 5
"""
m = list(map(int, input().split()))  # read the list of the process
x = [i + 1 for i in range(len(m))]
m = list(zip(x, m))
n = int(input("enter the number of the process to be allocated memory"))
a = []
for i in range(n):
    x = int(input())
    a.append([i + 1, x])


# this will read the process memory to be allocated

# lets create a function to get the acurate of the rearest element

def find(n, a):
    x = [(a[i], a[i][1] - n) for i in range(len(a)) if (a[i][1] - n >= 0)]
    for i in range(len(x)):
        for j in range(0, len(x) - i - 1):
            if x[j][1] > x[j + 1][1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x[0][0]


# this will return the least element near to the given element
for i in range(len(a)):
    x = find(a[i][1], m)
    m.pop(m.index(x))
    a[i].append(x)
print(a)
for i in range(len(a)):
    print(a[i][0], "\t", a[i][1], "\t", a[i][2][0], "\t", a[i][2][1], "\t", a[i][2][1] - a[i][1])
