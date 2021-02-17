#3.Store a list of first names. Count the occurrences of ‘a’ within the list.




list=['aleena','megha','akhila','kavya']
count=0
for name in list:
    for i in name:
        if(i=='a'):
            count=count+1
print("The list is:",list)
print("occurrence of 'a': ",count)
