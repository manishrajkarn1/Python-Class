#Generate Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
a = 10
b= 20