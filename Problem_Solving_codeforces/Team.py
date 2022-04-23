from ast import And


input_Number = int(input())
count = 0
for i in range(0, input_Number):
    M = input()
    if M.count("1") >=2:
        count += 1
print(count) 