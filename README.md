
# DigitCounter 

A Python function designed to count the digits in the integer part of a number, whether it's an integer, float, fraction, decimal, or even a complex number. This function handles various edge cases, such as negative values, zero, and invalid inputs, and returns the number of digits in the absolute value of the integer part.

## Features

- **Handles multiple numeric types**: Works with integers, floats, fractions, decimals, and complex numbers.
- **Validates input**: Returns informative error messages for invalid inputs (including strings that can't be converted to a number).
- **Edge case handling**: Correctly counts digits for edge cases like negative numbers, zero, and large numbers.

## Usage

### Example Usage

```python
from your_module_name import count_integer_digits

print(count_integer_digits(123.456))        # Output: 3
print(count_integer_digits(-456.789))       # Output: 3
print(count_integer_digits("123.4567"))     # Output: 3
print(count_integer_digits(10**100))        # Output: 101
print(count_integer_digits("hello"))        # Output: "Invalid input 'hello'. Please provide a valid real number."
