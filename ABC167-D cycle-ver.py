n, k = map(int, input().split())
A = list(map(int, input().split()))

C = [0 for i in range(n)]   #Count
P = [-1 for i in range(n)]  #Patern
cp = 1  #current point
t = 0   #周期
while 1:
    #print('C = ', C)
    C[cp - 1] += 1
    if C[cp - 1] < 2:
        P[cp - 1] = t
    else:
        break
    cp = A[cp - 1]
    t += 1

pret = P[cp - 1]    #周期に入るまでの時間
t = t - pret
#print('pret = ', pret)
#print('t = ', t)
#print('P = ', P)

if k <= pret:
    l = k 
else:
    k = k - pret
    l = k % t
    P = list(map(lambda x: x - pret, P))
#print('P = ', P)

ans = 0
for i in range(n):
    if P[i] == l:
        ans = i + 1
        break
    else:
        pass
print(ans)