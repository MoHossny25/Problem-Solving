X = str(input())
Z = sum(1 for c in X if c.isupper())
C = sum(1 for c in X if c.islower())
if Z > C:
    print(X.upper())
else:
    print(X.lower())