"""Challenge_001-010.py
تكليفات الدروس من الدرس 026 إلى 032
https://elzero.org/python-assignments-lesson-from-26-to-32/
"""
# Challenge -1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
unique_list.remove(5)
print(unique_list)
print("#"*30)

    # Challenge -2
nums_2 = {1, 2, 3}
letters_2 = {"A", "B", "C"}
New_Set = nums_2.union(letters_2)
print(New_Set)
print(nums_2|letters_2)
# print(nums_2+letters_2) > Error.
print("#"*30)

        # Challenge -3
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
print(my_set.clear())
my_set.update("A","B")
print(my_set)
print("#"*30)

            # Challenge -4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("#"*30)

                # Challenge -5
my_Dec = {"Html":90,"Css":80,"Python":30}
dect = list(my_Dec.keys())[0]
dect_1 = list(my_Dec.keys())[1]
dect_2 = list(my_Dec.keys())[2]
print(F'{dect} Progress Is {my_Dec.get("Html")}%\n{dect_1} Progress Is {my_Dec.get("Css")}%\n{dect_2} Progress Is {my_Dec.get("Python")}%')
my_Dec.update({"Ai":20})
dect_3 = list(my_Dec.keys())[3]
print(F"{dect_3} progress Is {my_Dec.get('Ai')}%")