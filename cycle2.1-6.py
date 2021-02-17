#6. Count the number of characters (character frequency) in a string.



str=input("Enter the string: ")
dict={}
for n in str:
        keys=dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
print(dict)
