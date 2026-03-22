#function to get sum of all elements in the integer array getSum

def getSum(numbers):
    sum=0
    for number in numbers:
        sum+=number
    print(f"Sum of all elements :{sum}")

numbers=[]
for i in range(1,6):
    numbers.append(i)
print("numbers:",numbers)
getSum(numbers)