"""
تكليفات الدروس من الدرس 041 إلى 046
https://elzero.org/python-assignments-lesson-from-41-to-46/
"""
# Challenge -1
num1 = int(input("What's your Number First? ").strip())
num2 = int(input("What's your Number Second? ").strip())
operation = input("What's your operation? ").strip()
print(F"num1 {num1} operation {operation} num2 {num2}")
print(F"Example One {num1} {operation} {num2} = ")
print(F"Example Two {num1} {operation} {num2} = ")
# print("#"*30)

    # Challenge -2
age = 17
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")
print("#"*30)

        # Challenge -3
age_input = int(input().strip())
if age_input <100 and age_input > 10:
    print(F"Your age is in the year it is {age_input}\n,the month it {age_input*12}\n,the weeks it will be {age_input*12*4},")
    print(F"the days will be {age_input*12*4*365}\n,the hours will be {age_input*12*4*365*24},")
    print(F"the minutes will be {age_input*12*4*365*24*60}\n,the seconds will be {age_input*12*4*365*24*60*60}")
    print("#"*30)
else:
    print("Age is out of range.")
            # Challenge -4
country = input("Input Your Country? ").capitalize().strip()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(F"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
else:
    print(F"Your Country Not Eligible For Discount And The Price Is ${price}")