"""
تكليفات الدروس من الدرس 011 إلى 018
https://elzero.org/python-assignments-lesson-from-11-to-18/
"""
# Challenge -1
N = "mohamed Hossny Hussein"
A = "20"
C = "Elwasta"
print("Hello, '{}', How You Doing \  Your Age Is {} + And Your Country Is: {}".format(N,A,C))            
print("#"*30)

    # Challenge -2
print("Hello, '{}', How You Doing \  \nYour Age Is {} + \nAnd Your Country Is: {}".format(N,A,C))            
print("#"*30)

        # Challenge -3
name = 'Elzero'
print(name[1])
print(name[2])
print(name[-1])
print("#"*30)
            # Challenge -4
print(name[1:4])
print(name[0:5:2])
print(name[4]+name[2]+name[0])
print("#"*30)

                # Challenge -5
name = "#@#@Elzero#@#@"
print(name.replace('#@#@', ''))
print("#"*30)

                    # Challenge -6
num = "9"
num1 = "15"
num2 = "130"
num3 = "950"
num4 = "1500"
print(num.zfill(4))                 
print(num1.zfill(4))                 
print(num2.zfill(4))                 
print(num3.zfill(4))                 
print(num4.zfill(4))                 
print("#"*30)

                        # Challenge -7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(21,'$'))
print(name_two.rjust(21,'$'))
print("#"*30)

                            # Challenge -8
name_3 = "OSamA"
name_4 = "osaMA"
print(name_3.swapcase())
print(name_4.swapcase())
print("#"*30)

                                # Challenge -9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))
print("#"*30)

                                    # Challenge -10
name_5 = "Elzero"
print(name_5.index('z'))
print("#"*30)

                                        # Challenge -11
msg_1 = "I <3 Python And Although <3 Elzero Web School"
print(msg_1.replace('<3', 'Love',1))
print("#"*30)
                                            # Challenge -12
msg_2 = "I <3 Python And Although <3 Elzero Web School"
print(msg_2.replace('<3', 'Love'))
print("#"*30)                               
                                                # Challenge -13
name_11 = "Mo7amed-7ossny"
age_11 = 20
country_11 = "Egypt"
print(F"My Name Is {name_11}, And My Age Is {age_11}, And My Country Is {country_11}")