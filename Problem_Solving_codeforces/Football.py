X = input()

a = '1111111'
s = '0000000'

search_1 = X.count('1111111')
search_2 = X.count('0000000')
if search_1 or search_2 > 0 :
    print('YES')
else:
    print('NO')