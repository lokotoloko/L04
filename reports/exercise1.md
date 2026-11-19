# Bug reports for exercise1.py

Line: 3
Problem: The function checks if n % 2 == 1, which is true for odd numbers, not even numbers. The docstring says it should return true for even numbers.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, not the product, which is required for rectangle area.
Example: rectangle_area(5, 3) returns 8, expected 15.
Fix: return width * height

Line: 12
Problem: The function adds 2 to n, but the docstring says it should return twice the number.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
