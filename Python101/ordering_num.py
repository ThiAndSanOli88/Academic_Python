# This program will get 3 possitive number from user and ordering. 
# Coleting numbers from the user:
while True:
  num1 = input('Plese enter your first possitive number:==>   ')
  num2 = input('Plese enter your Second possitive number:==>   ')
  num3 = input('Plese enter your Third possitive number:==>   ') # Analise the numbers and validade it.
  if num1.isnumeric() and num2.isnumeric() and num3.isnumeric():
      num1,num2,num3 = int(num1), int(num2), int(num3)
  if num1 >= 0 and num2 >= 0 and num3 >= 0:
      break
  else:
      print ("Please enter only positive number!")
        
# If user input valid positive number the sistem will print it in ascending order. 
if num1 <= num2 <= num3: 
    print("Numbers in ascending order:", num1, num2, num3)
elif num1 <= num3 <= num2: 
    print("Numbers in ascending order:", num1, num3, num2)
elif num2 <= num1 <= num3:
    print("Numbers in ascending order:", num2, num1, num3)
elif num2 <= num3 <= num1: 
    print("Numbers in ascending order:", num2, num3, num1)
elif num3 <= num1 <= num2:
    print("Numbers in ascending order:", num3, num1, num2)
elif num3 <= num2 <= num1:
    print("Numbers in ascending order:", num3, num2, num1)
    
print ("The End!")