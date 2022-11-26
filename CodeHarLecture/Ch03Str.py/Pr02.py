letter = '''Dear <|Name|>,

You Are Selected

Date: <|Date|>
'''


Name=input("Enter Your Name: ")
Date=input("Enter Date: ")
letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)
print(letter)
