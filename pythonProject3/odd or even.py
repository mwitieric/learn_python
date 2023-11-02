number = int(input("Enter a number to check if its even or a multiple of 4 :"))

if number%4 == 0:
    print(f"{number} is a multiple of 4")
elif number%2 == 0:
    print(f"{number}is even")
else:
    print(f"{number}is odd")

