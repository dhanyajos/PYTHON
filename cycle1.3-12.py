
#12. From a list of integers, create a list removing even numbers
 




num = [17,80, 12, 25, 44, 21, 37]
new=[]
print(num)
for i in num:
       if(i%2!=0):
           new.append(i)
print("After removing even numbers:",new)

