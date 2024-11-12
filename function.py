from typing import Union
from decimal import Decimal
from fractions import Fraction

def count_integer_digits(number: Union[int, float, Decimal, Fraction]) -> int:
    """
    This function counts the digits in the integer part of a given number provided by the user.
    It returns the number of digits in the integer component, ignoring any fractional part or sign.

            Parameters
            ----------
            number : int, float, Decimal, or Fraction
                The number whose integer part's digits are to be counted.

            Returns
            -------
            int
                The count of digits in the integer part of the number.
            """
    #Handling invalid cases
    if isinstance(number, str):
        try:
            number = float(number)  # Try to convert the string to a float
        except ValueError:
            return f"Invalid input '{number}'. Please provide a valid real number."  # Return error message directly

    # Handling special cases like fractions and decimals
    if isinstance(number, Fraction):
        number = number.numerator // number.denominator
    elif isinstance(number, Decimal):
        # Converting to integer part of decimal
        number = int(number.to_integral_value())
    elif isinstance(number, complex):
        # Use the real part of complex numbers
        number = abs(number.real)

    # Ensuring we only handle valid numeric types now
    if not isinstance(number, (int, float, Decimal, Fraction)):
        return "Input must be an integer, float, Decimal, Fraction, or a string representing a number."

    # Using the integer part of the absolute value to ignore sign and fraction
    integer_part = abs(int(number))

    # Counting digits by converting to string and getting length
    return len(str(integer_part))











