#1.Create a string from given string where first and last characters exchanged. [eg: python -&#gt; nythop]



str=input("Enter a string: ")
start=str[0]
end=str[-1]
str=end+str[1:-1]+start
print(str);
