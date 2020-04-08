n, m = map(int, input().split())

flag = True
Place = [-1] * n
for i in range(m):
    s, c = map(int, input().split())
    #指定桁を決定
    if Place[s-1] == c or Place[s-1]== -1: 
        Place[s-1] = c
    else:   #異なる数字が同一の桁で指定されている
        flag = False

ans = 0
for i in range(n):
    if n == 1 and Place[i] <= 0:   #1桁で未指定or最上位桁0
        Place[i] = 0
    else:
        if i == 0:  #最上位桁
            if Place[i] == 0:
                flag = False
            elif Place[i] == -1:    #未指定
                
                Place[i] = 1
            else:
                pass
        else:
            if Place[i] == -1:  #未指定
                Place[i] = 0
            else:
                pass
    ans += Place[i] * (10 ** (n-1-i))

if flag == True:
    print(ans)
else:
    print(-1)


        

