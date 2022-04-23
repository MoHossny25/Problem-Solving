"""Program to reverse any word like <code> to <edoc>"""

t = str(input()).lower().strip()
s = str(input()).lower().strip()
stringlength = len(t)
the_condition = t[stringlength::-1]
if s == the_condition:
    print("YES")
else:
    print("NO")