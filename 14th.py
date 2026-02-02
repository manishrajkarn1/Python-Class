# Check whether a number is prime.
num = int(input("Enter the number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")
