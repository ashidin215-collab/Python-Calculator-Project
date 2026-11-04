def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "error:0 se divide nahi kar sakte" 
    return x/y
def rem(x,y):
    return x%y
def avg(x,y):
    return x+y/2

print("Simple Calulator")
print("Operation:")
print("1.Add(+)")
print("2.subtract(-)")
print("3.multiply(*)")
print("4.Divide(/)")
print("5.rem(%)")
print("6.avg(x+y/2)")

choice=input("Konsa operation karna ha(1/2/3/4):")

num1=int(input("Pehla num dijiya:"))
num2=int(input("Dusra num dijiya:"))



if choice == "1":
    print("Result:",add(num1,num2))
elif choice == "2":
    print("Result:",subtract(num1,num2))    
elif choice == "3":
    print("Result:",multiply(num1,num2))
elif choice == "4":
    print("Result:",divide(num1,num2))
elif choice=="5":
    print("Result:",rem(num1,num2))
elif choice=="6":
    print("Result:",avg(num1,num2))
else:
    print("Galat choice")




