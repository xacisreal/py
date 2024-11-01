n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
print(a, end=" ")
a, b = b, a + b  # Update values for next iteration
