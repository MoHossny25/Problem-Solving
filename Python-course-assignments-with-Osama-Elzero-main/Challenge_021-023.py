"""
تكليفات الدروس من الدرس 021 إلى 023
https://elzero.org/python-assignments-lesson-from-21-to-23/

"""
# Challenge -1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(F"The first element of list are (Method-1): {friends[0]}")
print(F"The first element of list are (Method-2): {friends[-5]}")
print(F"The Last element of list are (Method-1): {friends[4]}")
print(F"The Last element of list are (Method-1): {friends[-1]}")
print("#"* 30)

    # Challenge -2
friends_0 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends_0[::2])
print(friends_0[1::2])
print("#"* 30)

        # Challenge -3
friends_1 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(F'"{friends_1[1]}", {friends_1[2]}", "{friends_1[3]}"')
print(F'"{friends_1[-2]}", "{friends_1[-1]}"')
print("#"* 30)

            # Challenge -4
friends_2 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends_2[-2] = "Elzero"
friends_2[-1] = "Elzero"
print(friends_2)
print("#"* 30)

                # Challenge -5
friends_3 = ["Osama", "Ahmed", "Sayed"]
friends_3.append("Kinda")
friends_3.insert(0, "Hossny")
print(friends_3)
print("#"* 30)

                    # Challenge -6
friends_6 = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends_6.remove("Nasser")
friends_6.remove("Osama")
print(friends_6)
friends_6.pop()
print(friends_6)
print("#"* 30)

                         # Challenge -7

friends_7 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends_7.extend(employees)
friends_7.extend(school)
print(friends_7)
print("#"* 30)

                            # Challenge -8
friends_8 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends_8.sort()
print(friends_8)
friends_8.sort(reverse=True)
print(friends_8)
print("#"* 30)

                                # Challenge -9
friends_9 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends_9))
print("#"* 30) 
    
                                    # Challenge -10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])