
#2.Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.




list=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    elem=int(input("Enter the element: "))
    if(elem>100):
        list.append("over")
    else:
        list.append(elem)
print(list)      
