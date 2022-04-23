N = int(input())

xx = yy = zz = 0

for i in range(0, N):
    X, Y, Z = map(int,input().split())
    xx += X
    yy += Y
    zz += Z

if xx == yy == zz  == 0:
    print("YES")
else:
    print("NO")