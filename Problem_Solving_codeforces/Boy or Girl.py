username = input()
length = len(username)
username = list(username)
number_distinct = 0
count = 0
stored = []
for i in username:
    if username.count(i) > 1:
        if i in stored:
            pass
        else:
            number_distinct -=1
            stored.append(i)
    elif username.count(i) <= 1:
        number_distinct +=1
if number_distinct  & 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
    