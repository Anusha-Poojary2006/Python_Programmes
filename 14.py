#function to merge two arrays and return combined output in first array

def merge(list1,list2)->list[int]:
    for num in list2:
        list1.append(num)
    
    return list1

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
result=merge(list1,list2)
print("list 1 elements are:",result)
