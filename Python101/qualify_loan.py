#Get the custumer income
custumer_income = input('How much is your income per year: ')

total_income = float(custumer_income)

#Compair if the custumer income is qualify with the minimum requirement
if total_income >= 30000:
    years_imployed = float(input('How many years you are employed: ')) #Get the muber of years that the custumer is employed
    if total_income >= 30000 and years_imployed >= 2.0:
        print ('Your are qualify for the loan.')
    else:
        print('You are not qualify for the loan. You must have more than 2 years employed.')
else:
    print('You must have more than $30.000 income per year.')
#Result if the custumer is qualify or not.