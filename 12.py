#function to print max and min value from an integer array, printMaxMin

def printMaxMin(Numbers)->list[int]:
    Max=Numbers[0]
    Min=Numbers[0]
    for number in Numbers:
        if(number>Max):
            Max=number
        if(number<Min):
            Min=number
    print("Maximum number in integer array:",Max)
    print("Minimum number in integer array:",Min)

Numbers=[]
for i in range(0,5,1):
    num=int(input("Enter a number:"))
    Numbers.append(num)
printMaxMin(Numbers)