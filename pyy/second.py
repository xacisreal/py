import math
a=int(input("Enter the first no: "))
b=int(input("Enter the sec no: "))
c=int(input("Enter the third no: "))
n=max(a,b,c)
print(f"The biggest no is: {n}")

sum=n+int(f"{n}{n}")+int(f"{n}{n}{n}")
print(f"Sum : {sum}")

print(f"Area of a circle with radius {n}:{math.pi*n**2:.2f}")
print(f"Perimeter of a circle with radius {n}:{2*math.pi*n:.2f}")
print(f"Volume of a sphere with radius {n}:{(4/3)*math.pi*n**3:.2f}")


