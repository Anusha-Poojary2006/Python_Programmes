#function to search in an sorted integer array

def sorted(Numbers,key)->list[int]:
    Numbers.sort()
    left=0
    right=len(Numbers)-1
    found=False
    while(left<=right):
        mid=(int)((left+right)/2)
        if (key==Numbers[mid]):
            found=True
            break
        elif(key<Numbers[mid]):
            right=mid
        elif(key>Numbers[mid]):
            left=mid
        
    return found

Numbers=[]
for i in range(0,5,1):
    num=int(input("Enter a number:"))
    Numbers.append(num)
key=int(input("Enter a search key:"))
result=sorted(Numbers,key)
if(result):
    print("Key found")
else:
    print("key not found")
