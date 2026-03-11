# Function isEven to return true if number is even otherwise false

def isEven(num):
    if(num%2==0):
        return True
    else:
        return False
    
number=int(input("Enter a number:"))
result=isEven(number)

if(result):
    print(f"{number} is even")
else:
    print(f"{number} is odd")