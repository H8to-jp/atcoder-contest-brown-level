#定数
#1≦k≦n≦2*10^5
n , k = map(int, input().split())
#1≦P[i]≦10^3
#O(n)
P = list(map(int, input().split()))

#サイコロの目が1~numの期待値を求める関数
#O(1)
def dice_expectations(num:int)->float:
    return (num+1) / 2

#O(n)
E = list(map(dice_expectations, P)) #Expectations

#k個ずつ
tmp = sum(E[0:k])
ans = 0
#O(n-k+1)
for i in range(n-k+1):
    if tmp > ans:
        ans = tmp
    else:
        pass
    if i != n-k:
        tmp -= E[i]     #先頭のサイコロを取り除き
        tmp += E[k+i]   #次のサイコロを追加する
    else:
        pass

print(ans)  #O(n)