def is_armstrong_number(number: int):
    num_str = str(abs(number))
    total_digits = len(num_str)

    if total_digits > 10:
        print("Please, insert a number between 0 and 9.999.999.999")
        return None

    armstrong_sum = sum(int(digit) ** total_digits for digit in num_str)
    return armstrong_sum == number

def final_message(number):
    result = is_armstrong_number(number)
    if result is None:
        print("Invalid input.")
    elif result:
        print(f"{number} is an armstrong number!")
    else:
        return print (f"{number} is **not** an armstrong number")

## Testing the code
is_armstrong_number(153)
