def student_login():
    first_name = input('Plese enter your first name: ')
    last_name = input('Please enter you last name: ')
    student_number = input('Please enter your student number: ')

    set1 = first_name[0:3]
    set2 = last_name[0:3]
    set3 = student_number[-3:]

    login_name = set1 + set2 + set3

    print(login_name)
student_login()