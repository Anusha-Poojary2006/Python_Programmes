#function to second largest element in an integer array getSecondLargest

def getSecondLargest(Numbers)->list[int]:
    maxfirst=float('-inf')
    maxsecond=float('-inf')
    for num in Numbers:
        if(num>maxfirst):
            maxsecond=maxfirst
            maxfirst=num
        elif((num>maxsecond) ):
            maxsecond=num
    return maxsecond


Numbers=[]
n=int(input("Enter the size of the array:"))
for i in range(0,n,1):
    num=int(input("Enter a number:"))
    Numbers.append(num)
result=getSecondLargest(Numbers)
print(f"Second largest number in the list is:{result}")