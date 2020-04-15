#定数
#1≦a,b≦10^9 1≦x≦10^18
a, b, x = map(int, input().split())

#整数xが買えるかどうかを判定する関数
def judgement(n:int)->bool:
    d = len(str(n)) #digit
    if a*n + b*d <= x:
        #買える
        return True
    else:
        #買えない
        return False
#二分探索でTrueの最大を
def binary_search(l:int, r:int)->int:   #l:left, r:right
    while r - l > 1:
        t = (l + r) // 2  #target
        f = judgement(t)    #flag
        if f == True:
            l = t
        else:
            r = t
        print(l)
        print(r)
    return l    

print(binary_search(0, 10**9+1))    #すべてTrueとなったら10^9が帰ってくる