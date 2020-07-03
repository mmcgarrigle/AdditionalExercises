number1 = int(input("enter number here: "))
number2 = int(input("enter number here: "))

def function(number1,number2):
    if (number1 + number2) % 2 == 0:
        return(int(number1 + number2))
    else:
        return(int(number1 * number2))