#basic calculator

def add(a,b):
    print(a,"+",b," = ",a+b,"\n")
def subtract(a,b):
    print(a,"-",b," = ",a-b,"\n")
def multiply(a,b):
    print(a,"*",b," = ",a*b,"\n")
def divide (a,b):
    if(b!=0):
        print(a,"/",b," = ",a/b,"\n")
    else:
        print(a,"/",b, "= not defined")
def power(a,b):
    print(a,"^",b," = ",a**b,"\n")
    
print("-----CALCULATOR MENU-----\nA to add\nS to subtract\nM to multiply\nD to divide\nE for exponent\nQ to quit\n")

while True:
    op=str(input("Enter operation letter: "))
    if(op=="a" or op=="A"):
        num1=float(input("Enter first operand: "))
        num2=float(input("Enter second operand: "))
        add(num1,num2);
    elif(op=="s" or op=="S"):
        num1=float(input("Enter first operand: "))
        num2=float(input("Enter second operand: "))
        subtract(num1,num2)
    elif(op=="m"or op=="M"):
        num1=float(input("Enter first operand: "))
        num2=float(input("Enter second operand: "))
        multiply(num1,num2)
    elif(op=="d" or op=="D"):
        num1=float(input("Enter first operand: "))
        num2=float(input("Enter second operand: "))
        divide(num1,num2)
    elif(op=="e" or op=="E"):
        num1=float(input("Enter first operand: "))
        num2=float(input("Enter second operand: "))
        power(num1,num2)
    elif(op=="q"or op=="Q"):
        print("Leaving calculator, thank you!")
        break
    else:
        print("Invalid input! Try again")