from bisect import bisect_left
n = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        b = L[i] + L[j]
        ans += bisect_left(L, b) - 1 - j 
print(ans) 