first_input = str(input())
second_input = str(input())
three_input = str(input()).upper()

X = first_input + second_input
F = sorted(X)
f_string = "".join(F) 

S = sorted(three_input)
s_string = "".join(S)

if f_string == s_string :
    print("YES")
else:
    print("NO")

        # An other way
# print("YES" if f_string == s_string else "NO")