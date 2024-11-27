color_list1=input("Enter the set of colours:").split(",")
print(f"First color: {color_list1[0]}")
print(f"Last color: {color_list1[-1]}")
color_list2=input("Enter another set of colours").split(",")
unique=[color for color in color_list1 if color not in color_list2]
print("Colours in first not in second: ",unique)
color_final={index+1:color  for index,color in enumerate(color_list1)}
print("Final colour list: ",color_final)