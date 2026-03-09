# function swapnumbers to swap two variable values
 
def swapNumbers(a,b):
    temp=a
    a=b
    b=temp
    return a,b

value1=10
value2=20

print(f"Before swapping a={value1},b={value2}")
value1,value2=swapNumbers(value1,value2)
print(f"After swapping a={value1},b={value2}")


