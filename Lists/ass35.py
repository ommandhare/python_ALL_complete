# Get input number from user
user_number = int(input("Enter a number: "))
# Get the digit to count occurrences
digit_to_count = int(input("Enter the digit to count: "))

# Convert the number to a string to iterate through its digits
number_str = str(user_number)

# Count the occurrences of the specified digit
occurrences = 0
for digit in number_str:
    if int(digit) == digit_to_count:
        occurrences += 1

# Print the number of occurrences
print(f"The digit {digit_to_count} appears {occurrences} time(s) in the number {user_number}.")
