input_number_1 = int(input())
x = 0

for i in range(input_number_1):
    j = input()
    if '++' in j:
        x = x + 1
    else:
        x = x - 1    
print(x)