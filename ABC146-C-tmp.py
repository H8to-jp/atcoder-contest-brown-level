#定数
#1≦a,b≦10^9 1≦x≦10^18
a, b, x = map(int, input().split())

d = 1   #digit
j = a + b   #judge number
#桁数を確定させる
while j < x:
    d += 1
    #10^dの価格
    j = a*(10**(d-1)) + b*d
#大きいほうが出てくるから
d -= 1

#整数を確定させる
if d >= 10:
    print(10**9)
else:
    n = (x - b*d) // a
    if n >= 10**d:
        print((10**d)-1)
    else:
        print(n)
