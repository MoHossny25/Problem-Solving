from math import ceil

n,m,a=map(int,input().split()) 

if m % a == 0 :
    x_1 = m // a
else:
    x_1 = m // a + 1

if n % a == 0 :
    z_1 = n // a
else:
    z_1 =  n // a + 1

print(x_1 * z_1)