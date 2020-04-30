n = int(input())
L = sorted(list(map(int, input().split())), reverse = True)

# c < b < a の条件下
def judge(a:int, b:int, c:int):
    if a < b + c:
        pass
    else:
        return False
    return True

def binary_search(l:int, r:int):
    while r - l > 1:
        mid = (l + r) // 2
        c = L[mid]
        if judge(a, b, c) == True:
            l = mid
        else:
            r = mid
    return l

ans = 0
for i in range(n - 2):
    a = L[i]
    for j in range(i + 1, n - 1):
        b = L[j]
        f1 = judge(a, b, L[j + 1])
        f2 = judge(a, b, L[n - 1])
        if f1 == True:
            if f2 == False:
                ans += binary_search(j, n - 1) - j 
            else:
                ans += n - j - 1
        else:
            pass
    
print(ans)