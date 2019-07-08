def pythoncalc():
    operation = input('\n'+'''	Python Basic Calculator
	For Addition, Subtraction, Division, Multiplication
	-----------------------------------------------------
	
	Welcome to Python Calculator!
	Please choose the operation below.
	1. Addition
	2. Subtraction
	3. Division
	4. Multiplication
	
	Please choose the operation!
	User input: ''')

    number_1 = float(input('\n'+'Please enter the first number: '))
    number_2 = float(input('Please enter the second number: '))

    if operation == '1':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '2':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '3':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '4':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    else:
        print('Operator not found and/or invalid input, please try again!')

	
    repeat()

def repeat():
    calc_repeat = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
User input: ''')

    if calc_repeat.upper() == 'Y' or 'y':
        pythoncalc()
    elif calc_repeat.upper() == 'N' or 'n':
        print('\n'+'Thank you for using this program!')

pythoncalc()