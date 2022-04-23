X = int(input())
for i in range(0, X):
    C = str(input())
    Z = str(len(C)-2)
    if len(C)>10:
        print(f"{C[0]+Z+C[-1]}")
    else:
        print(C)