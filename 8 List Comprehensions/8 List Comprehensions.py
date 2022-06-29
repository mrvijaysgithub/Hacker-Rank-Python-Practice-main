x = int(input())
y = int(input())
z = int(input())
n = int(input())
arr = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            arr.append([i,j,k])
temp = tuple(arr) 

for s in temp:
    
    if sum(s)==n:
        
        arr.remove(s)
print(arr)
