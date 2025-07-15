pattern_number = int(input("Enter the size of the pattern:"))
num = 0

while num < pattern_number:
    num += 1
    for j in range(1, pattern_number + 1):
        print("*", end="")
    print()  # Move to the next line after each row