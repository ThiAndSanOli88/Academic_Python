""" 
Write a program that ask the user their name and their favorite number.  
Display their name, their favorite number and their favorite number multiplied by 99 on 3 lines.
"""
name = input("What is your name?--> ")
print(name + " , nice to meet you!")
print("My name is Python, now tha we know each other, I have a question for you.")
favorite_number = input("What is your favorite number?--> ")
favorite_number_multiplied = int(favorite_number) * 99
print("Your favorite number is " + favorite_number)
print(name + " Your favorite number multiplied by 99 is ", favorite_number_multiplied)