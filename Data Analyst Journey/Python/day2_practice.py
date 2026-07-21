#Create a calculator using functions.

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print(' press 1 for addition')
print(' press 2 for subtraction')
print(' press 3 for multiply')
print(' press 4 for divide')



while True:
    choice = input("Enter your choice (1/2/3/4) :- ")
    if choice in ('1','2','3','4'):
        num1 = float(input('Enter first num :- '))
        num2 = float(input('Enter second num :- '))
        if choice == '1':
         print(f'{num1} + {num2} =  {addition(num1,num2)}')
        elif choice == '2':
            print(f'{num1} - {num2} =  {subtraction(num1,num2)}')
        elif choice == '3':
            print(f'{num1} * {num2} =  {multiply(num1,num2)}')
        elif choice == '4':
            print(f'{num1} / {num2} =  {divide(num1,num2)}')

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
      
