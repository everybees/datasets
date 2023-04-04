# takes in an integer number and print out the number in words

# one - nine
# ten
# twenty
# thirty
# fourty
# fifty
# sixty
# seventy
# eighty
# ninety
# hundred
# 11 - 13
# teens 14 - 19

single_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
magic_teens = ['eleven', 'twelve', 'thirteen']
double_digits = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eigthy', 'ninety']
four_digits = ['thousand']

number = '205'

def numbers(digits, number):
    if digits == 1:
        return single_digits[int(number)]
    elif digits == 2 and number in ['11', '12', '13']:
        return magic_teens[int(number[1])-1]
    elif digits == 2 and number[1] == '0':
        return double_digits[int(number[0])-1]
    elif digits == 2 and number[0] == '1':
        return f"{single_digits[int(number[1])]}teen"
    elif digits == 2 and number[0] == '0':
        return single_digits[int(number[1])]
    elif digits == 2:
        return f"{double_digits[int(number[0])-1]}-{single_digits[int(number[1])]}"


def hundreds(digits, number):
    return f"{single_digits[int(number[0])]}-hundred-and-{numbers(digits-1, number[1:])}"


def func(number):
    digits = len(number)
    if digits < 3:
        return numbers(digits, number)
    elif digits == 3:
        return hundreds(digits, number)
    # else:
    #     return f"{single_digits[int(number[0])]}-thousand-{hundreds(digits-1, number[1:])}"



print(func(number))
