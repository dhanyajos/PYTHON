#2. Accept a list of words and return length of longest word.


a=[]
n= int(input("Enter the number of words in list:"))
for x in range(0,n):
    element=input("Enter the word:")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The longest word is:",temp)
print("The length of the longest word is:",len(temp))

