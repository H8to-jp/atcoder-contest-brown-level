import collections
#定数
n = int(input())
S = input()

#ここの計算量は？
#R,G,Bそれぞれの出現回数
C = collections.Counter(S)
r = C['R']
g = C['G']
b = C['B']
#条件1
ans = r * g * b

#最大O(n^2)
for j in range(1, n-1):
    sj = S[j] 
    if j > n-1-j:
        a = n-1-j
    else:
        a = j
    for d in range(1, a+1):
        si = S[j-d]
        sk = S[j+d]
        if si != sj and si != sk and sj != sk:
            #条件2を満たさないが条件1を満たすもの
            ans -= 1
        else:
            pass
print(ans)





