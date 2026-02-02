#Find the largest of three numbers.
num = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
num3 = int(input("Enter the number:"))

if num > num2 or  num > num3:
        print(f"{num} is the largest number.")
elif num2 > num or  num2 > num3:
        print(f"{num2} is the greates number.")
else:
        print(f"{num3} is the greatest number.")

