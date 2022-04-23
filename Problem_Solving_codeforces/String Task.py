
string_input = str(input( )).lower()

new_input = string_input.replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')

X = "." + '.'.join(new_input)

print(X)