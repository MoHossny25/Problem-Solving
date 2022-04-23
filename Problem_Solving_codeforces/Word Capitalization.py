from turtle import title


Input_String = str(input())
Word = Input_String[0]

if Word == Word.capitalize():
    print(Input_String)
else:
    print(f'{Word.capitalize()}{Input_String[1:]}')
