def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
operations_dict={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
    '%':mod
}
num1=int(input("Enter first number: "))
for symbol in operations_dict:
    print(symbol)
operator=input("Enter operator: ")
num2=int(input("Enter second number: "))
if operator=='+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operator=='-':
    print(f"{num1} - {num2} = {sub(num1,num2)}")
elif operator=='*':
    print(f"{num1} * {num2} = {mul(num1, num2)}")
elif operator=='/':
    print(f"{num1} / {num2} = {div(num1, num2)}")
elif operator=='%':
    print(f"{num1} % {num2} = {mod(num1, num2)}")
else:
    print("Enter only arithmetic opperations")