
#4.Form a list of vowels selected from a given word.






new=input("Enter any word:")                                  #reading a word from input
vowels=['a','e','i','o','u']                                  #declaring a list of vowels
list1=[]                                                                             
for x in new:                                                 #iterating each element in  new
    if (x in vowels and x not in list1):                      #checking the condition
        list1.append(x)                                                     
print("Vowels present in given word:",list1)
