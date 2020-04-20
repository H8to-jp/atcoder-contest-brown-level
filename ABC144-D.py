from math import atan2, degrees

a, b, x = map(int, input().split())

#二次元に落とし込む
s = x/a
#場合分け
if s >= a*b/2:
    z = 2*b - 2*x/a**2
    ans = degrees(atan2(z, a))
else:
    z = 2*x/(a*b)
    ans = 90-degrees(atan2(z, b))
print(ans)
