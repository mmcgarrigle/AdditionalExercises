number1 = int(input("enter number here: "))
number2 = int(input("enter number here: "))

def function(number1, number2):
    for i in range (1,11):
        if number1 == 0:
            return(number2)
        elif number2 == 0:
            return(number1)
        else:
            return(int(number1 + number2))