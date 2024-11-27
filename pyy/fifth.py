def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def fibonacci(n):
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def sum_of_list(lst):
    return sum(lst)

while True:
    print("\n1. Factorial\n2. Fibonacci series\n3. Sum of list")
    print("Press 'x' to exit")
    
    choice = input("Enter your choice: ")
    
    if choice == 'x'or choice=='X':
        print("Exiting the program. Goodbye!")
        break
    elif choice == '1':
        n = int(input("Enter a number: "))
        print(f"Factorial: {factorial(n)}")
    elif choice == '2':
        n = int(input("Enter number of terms: "))
        print(f"Fibonacci series: {fibonacci(n)}")
    elif choice == '3':
        lst = list(map(int, input("Enter list items : ").split()))
        print(f"Sum of list: {sum_of_list(lst)}")
    else:
        print("Invalid choice! Please choose again.")
