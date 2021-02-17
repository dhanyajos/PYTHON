#1.Count the occurrences of each word in a line of text.





def word_count(str):
    words=str.split()
    counts=dict()
    for word in words:
        if word in counts:
            counts[word]=counts[word]+1
        else:
            counts[word]=1
    return counts

new=input("Enter a string: ")
print(word_count(new))


