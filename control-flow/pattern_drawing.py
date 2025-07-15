pattern_number = int(input("Enter the size of the pattern:"))

for i in range(1, pattern_number + 1):
    for j in range(1, pattern_number + 1):
        print("*", end="")
    print()  # Move to the next line after each row