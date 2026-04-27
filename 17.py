# function to print intersection or common elements of two integer arrays getCommonElements

def getCommomElements(list1,list2)->list[int]:
     for i in range(0,len(list1),1):
        isFound=False
        for j in range(0,len(list2),1):    
            if(list1[i]==list2[j]):
                isFound=True
                break
        if(isFound==True):
            print(list1[i])


list1=[]
n1=int(input("Enter the size of the array:"))
for i in range(0,n1,1):
    num1=int(input("Enter a number:"))
    list1.append(num1)
list2=[]
n2=int(input("Enter the size of the array:"))
for i in range(0,n2,1):
    num2=int(input("Enter a number:"))
    list2.append(num2)
getCommomElements(list1,list2)
