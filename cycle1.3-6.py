#6.Accept an integer n and compute n+nn+nnn. 







n=int(input("Enter a number n:"))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)
