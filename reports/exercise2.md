# Bug reports for exercise2.py

Line: 3
Problem: The docstring says "True if the grade is 5 or more", but the function uses > 5, which excludes 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The docstring requires "at least 8 characters", but the function uses > 8, which excludes 8 characters.
Example: is_valid_password("abcdefg1") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The function incorrectly uses min(x, low) and then max(low, min(x, low)), which simplifies to low, making it always return low regardless of x.
Example: clamp(10, 1, 5) returns 1, expected 5.
Fix: return max(low, min(x, high))
