from calculations import calculate

loop_cal = 'yes'
while loop_cal.lower() == 'yes':
    result = None

    first_number = input('Insert first number: ')
    while not first_number.replace('.', '', 1).lstrip('-').isnumeric():
        print('Wrong input')
        first_number = (input('Insert first number: '))

    available_operations = '+ - * / ** √'
    print(f'available_operations: {available_operations}')
    operation = input('Choose operation: ')  # + - * / ** √
    operation_list = ['+', '-', '*', '/', '**', '√']
    while operation not in operation_list:
        print('Invalid choice')
        operation = input('Choose operation: ')

    if operation != '√':
        second_number = input('Insert second number: ')
        while not second_number.replace('.', '', 1).lstrip('-').isnumeric():
            print('Wrong input')
            second_number = (input('Insert second number: '))

        first_number = float(first_number)
        second_number = float(second_number)

        if operation == '/' and second_number == 0:
            print('Cannot divide with zero')
            break

        result = calculate(first_number, operation, second_number)

    else:
        first_number = float(first_number)
        result = calculate(first_number, operation)

    print(f'Result: {result}')

    loop_cal = input('Do you want another one? yes/no:')
    while loop_cal.lower() != 'no' and loop_cal.lower() != 'yes':
        print('Invalid choice')
        loop_cal = input('Do you want to play again? yes/no: ')

    if loop_cal.lower() == 'no':
        print('Have a nice day')
        exit()
