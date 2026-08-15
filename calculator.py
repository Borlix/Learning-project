def add(a , b):
    return a+b
def sub(a , b):
    return a-b
def multiply(a , b):
    return a*b
def divide(a , b):
    if b==0:
        return "Error : we can't devide by zero" 
    return a/b 

def calculator( ):
    print("...SIMPLE CALCULATOR...")
    print("Choose Opretaion : +  -  * / ")
    print("Enter 'q' on operator to quit  anytime" )
    history = []
    while True:

        try:
            num1 = float(input("Enter number 1st : "))
            num2 = float(input("Enter number 2nd : "))
            op = input("Enter Your Opration : ")
        except ValueError:
            print("Enter valid numbers!")
            continue 

        if op == 'q':
            print("\n--- History ---")
            for item in history:        
                print(item)
            print("Bye Have Great Day!")
            break

        if op == "+":
            result = add(num1 , num2)
        elif op == "-":
            result = sub(num1,num2)    
        elif op == "*":
            result = multiply(num1,num2)    
        elif op == "/":
            result = divide(num1,num2)    

        else :
            print("Invalid Operator !")
            continue
        history.append(f"{num1} {op} {num2} = {result}")
        print(f"result : {num1} {op} {num2} = {result}\n")
    
calculator() 