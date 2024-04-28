def generate_codes(number, mapping, current_code='', index=0, result=[]):
    if index == len(number):
        result.append(current_code)
        return

    digit = int(number[index])
    for letter in mapping[digit]:
        generate_codes(number, mapping, current_code + letter, index + 1, result)

    return result

def main():
    mapping = {
        0: [' '],
        1: ['a', 'b', 'c'],
        2: ['d', 'e', 'f'],
        3: ['g', 'h', 'i'],
        4: ['j', 'k', 'l'],
        5: ['m', 'n', 'o'],
        6: ['p', 'q', 'r', 's'],
        7: ['t', 'u', 'v'],
        8: ['w', 'x', 'y', 'z'],
        9: [' ']
    }

    number = input("Enter a number: ")

    codes = generate_codes(number, mapping)
    print("All possible codes:", codes)

if __name__ == "__main__":
    main()
