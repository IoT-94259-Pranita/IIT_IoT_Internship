num1=int(input("enter first number="))
num2=int(input("enter second number="))
def add(num1,num2):
    add=num1+num2
    return add
def sub(num1,num2):
    sub=num1-num2
    return sub
def mul(num1,num2):
    mul=num1*num2
    return mul
def div(num1,num2):
    div=num1/num2
    return div
while True:
    print("\nCalculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice==1:
        print("result=",add(num1,num2))
    elif choice==2:
        print("result=",sub(num1,num2))
    elif choice==3:
        print("result=",mul(num1,num2))
    elif choice==4:
        if num2==0:
            print("Error:division by zero")
        else:
            print("result=",div(num1,num2))
    else:
        print("Invaild choice")
            
    if choice == 5:
        break