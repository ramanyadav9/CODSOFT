#defining the function for calculator
#rmana chnagess
def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplicaton(a,b):
    return a * b
def divison(a,b):
    return a / b

def main():
    print("CALCULATOR!!".center(20))

    while True:
        #taking input from the keyword
        a = float(input("Enter the first number: "))  #first number
        b = float(input("Enter the second number: "))  #second number
        op = str(input('Selet the operator (+ , - , * , /): ')) #operator

        #call the function with the operator using
        if op == "+":
            print('The Addition is ', addition(a,b))

        elif op == "-":
            print('The Subtraction is ', subtraction(a,b))

        elif op == "*":
            print('The Multiplication is ', multiplicaton(a,b))

        elif op == "/":
            print('The Division is ', divison(a,b))

        else:
            print('invalid operator')
        again = input("Do you want to Calculate Again! (Y/N): ").strip().lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()