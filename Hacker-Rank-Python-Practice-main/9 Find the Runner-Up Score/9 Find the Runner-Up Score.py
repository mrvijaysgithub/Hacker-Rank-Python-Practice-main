def func (arr):
    r = set(arr)
    r.remove(max(r))
    return max(r)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ans = func(arr)
    print(ans)
