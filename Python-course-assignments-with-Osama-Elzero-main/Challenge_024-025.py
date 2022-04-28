"""
تكليفات الدروس من الدرس 024 إلى 025
https://elzero.org/python-assignments-lesson-from-24-to-25/
"""
# Challenge -1
Name = "Mohamed",
print(Name)
print(type(Name))
print("#"*30)

    # Challenge -2
friends_2 = ("Osama", "Ahmed", "Sayed")
y = list(friends_2)
y[0] = "Elzero"
friends_2 = tuple(y)
print(friends_2)
print(type(friends_2))
print(F"{len(friends_2)} Elements")
print("#"*30)

        # Challenge -3
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(F"{len(nums_and_letters_one)} Elements")
print("#"*30)

            # Challenge -4
my_tuple = (1, 2, 3, 4)
print(f"{my_tuple[0]}\n{my_tuple[1]}\n{my_tuple[3]}")
