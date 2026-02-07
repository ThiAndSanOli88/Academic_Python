import random

random.seed()
numbers_file = open('numbers.txt','w')

def randomlyPopulateNumbers():
     for count in range (100):
        random_number = random.randint(1,1000)
        numbers_file.write(f'{random_number}\n') 

randomlyPopulateNumbers()
numbers_file.close()
print('Data written to numbers.txt')