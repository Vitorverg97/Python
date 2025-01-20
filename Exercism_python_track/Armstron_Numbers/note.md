# Exemplo do Chat-GPT

```python
NUMBER = 153

def identifying_number(number):
    num_str = str(abs(number))
    total_digits = len(num_str)

    if total_digits > 4:
        print("Please, insert a number between 0 and 9999")
        return None

    armstrong_sum = sum(int(digit) ** total_digits for digit in num_str)
    return armstrong_sum == number

def is_armstrong_number():
    result = identifying_number(NUMBER)
    if result is None:
        print("Invalid input.")
    elif result:
        print(f"{NUMBER} is an Armstrong number!")
    else:
        print(f"{NUMBER} is **not** an Armstrong number!")

# Test the code
is_armstrong_number()
```
