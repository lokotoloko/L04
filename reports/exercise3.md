# Bug reports for exercise3.py

Line: 3
Problem: average crashes on empty list due to division by zero.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: first_word returns "" for empty text, but the docstring says "or "" if the text is empty", which is correct, but split() on empty string returns [], so [0] raises IndexError.
Example: first_word("") raises IndexError, expected ""
Fix: return text.split()[0] if text.strip() else ""

Line: 12
Problem: percent crashes on total=0 due to division by zero.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total != 0 else 0
