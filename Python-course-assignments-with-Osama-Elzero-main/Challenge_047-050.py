"""
تكليفات الدروس من الدرس 047 إلى 050
https://elzero.org/python-assignments-lesson-from-47-to-50/
"""
# Challenge -1
# num =int(input("What is the number? ").strip())
# if num > 0:
#     x = 0
#     while x in range(num):
#         x += 1
#         if x == 6 or x == 10:
#             continue
#         print(x) 
#     print(F"{x-2} Numbers Printed Successfully.")
# else:
#     print("Number 0 Is Not Larger Than 0")
# print("#"*30)

    # Challenge -2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i = 0
while i < len(friends):
    if friends[0][0] == friends[0][0].capitalize():
        continue
    print(friends[i])
    i = i + 1
