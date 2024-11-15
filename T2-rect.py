class Rectangle:
    def area(length, breadth):
        return length * breadth
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = Rectangle.area(length, breadth)
print("The area of the rectangle is:", area)
