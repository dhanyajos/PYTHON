#5.Get a string from an input string where all occurrences of first character replaced with ‘$’,except first character. [eg: onion -&gt; oni$n]



string=input("Enter a string:")
word=list(string)
ch=string[0]
length=len(string)
for i in range(1,length):
    if(word[i]==ch):
        word[i]='$'
print(word)        
    
