# function to print unique elements in an integer array  printUniqueElements

def printUniqueElements(Numbers,n):
    for i in range(0,n,1):
        isDuplicate=False
        for j in range(0,n,1):
            if(i==j):
                continue
            if(Numbers[i]==Numbers[j]):
                isDuplicate=True
                break
        if(isDuplicate==False):
            print(Numbers[i])


Numbers=[]
n=int(input("Enter the size of the array:"))
for i in range(0,n,1):
    num=int(input("Enter a number:"))
    Numbers.append(num)
printUniqueElements(Numbers,n)
