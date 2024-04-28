"""
get a number from user and check number of occurances of a single digit in that number.
 (for example. Num=7888, check number of occurances of digit 8 in number)

"""
user_number = int(input("Enter a number: "))

digit_to_count = int(input("Enter the digit to count: "))

number_str = str(user_number)

occurrences = 0
for digit in number_str:
    if int(digit) == digit_to_count:
        occurrences += 1


print(f"The digit {digit_to_count} appears {occurrences} time(s) in the number {user_number}.")
