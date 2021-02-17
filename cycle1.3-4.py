#4.Accept a file name from user and print extension of that





filename=input("Input the Filename: ")
file_ext = filename.split(".")
print("The extension of the file is: ",file_ext[-1])


