def calculate(x,opt,y):
    if opt=="+":
        return x+y
    elif opt=="-":
        return x-y
    elif opt=="*":
        return x*y
    elif opt=="/":
        if y!=0:
            return x/y
        else:
            return "Error: Division by zero"
    else:
        return "operator not found!!"

num1=float(input("Enter your first number:"))
num2=float(input("Enter your seceond number:"))
operator=input("choose between +,-,*,/:")
x=calculate(num1,operator,num2)
print (x)
