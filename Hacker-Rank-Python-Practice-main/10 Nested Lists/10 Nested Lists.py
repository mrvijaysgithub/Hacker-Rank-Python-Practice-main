N = int(input())

arr = []
for i in range(N):
    x = input()
    y = float(input())
    arr.append([x,y])
    
stg = []
num = []
for a,b in arr[:]:
    stg.append(a)
    num.append(b)

num = set(num)

num.remove(min(num))
m = min(num)
ans = []
for i in arr[:]:
    
    if i[1]==m:
        ans.append(i[0])

ans = set(ans)
for j in ans:
    print(j)
