"""
تكليفات الدروس من الدرس 038 إلى 040
https://elzero.org/python-assignments-lesson-from-38-to-40/
"""
# Challenge -1
name = input("what's your name? ")
print(F"Hello {name.strip().capitalize()}, Happy To See You Here.")
print("#"*30)

    # Challenge -2
my_age = int(input("what's your age? "))
print("#"*30)
if my_age < 16:
    print(F"Hello Your {my_age} Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(F"Hello Your Age Is {my_age}, All Articles Is Suitable For You")
        # Challenge -3
name_1 = input("what's your first name? ")
name_2 = input("what's your second name? ")
print(F"Hello {name_1.capitalize().strip()} {name_2[0].capitalize().strip()}.")
print("#"*30)

            # Challenge -4
email = input("What's your email? ").strip().lower()
print("your name is "+email[:email.index("@")].capitalize())
print("Email Service Provider Is " + email[email.index("@")+1:email.index(".")].capitalize())
print("Top Level Domain Is " + email[email.index(".")+1:])

