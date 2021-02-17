#5.Create a list of colors from comma-separated color names entered by user. Display first and last colors






a=input("Enter the colors:")
color_list=a.split(",")
print(color_list)
print("First color:",color_list[0])
print("Last color:",color_list[-1])

