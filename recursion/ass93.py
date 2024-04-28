"""
numbers and alphabets: assign 3 alphabets for each digit between 0 and 9.
Write a program to write all possible codes that can be generated for any user entered number.
For example: 1 - a,b,c and 2 - d,e,f then number 12 can be made as any of the codes: ad,ae,af,bd,be,bf,cd,ce,cf.

"""
def codes(number, alpha, current_code='', i=0, result=[]):
    if i == len(number):
        result.append(current_code)
        return

    digit = int(number[i])
    print(result)
    for letter in alpha[digit]:
        codes(number, alpha, current_code + letter, i + 1, result)

    return result



alpha={1:['a','b','c'],2:['d','e','f']}



number=input("Enter the number ")


output=codes(number,alpha)
print(output)
