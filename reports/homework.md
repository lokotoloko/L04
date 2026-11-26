# Bug reports for homework.py

Line: 8
Problem: is_even checks for odd numbers instead of even numbers.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 13
Problem: can_vote uses > 18 instead of >= 18, excluding 18.
Example: can_vote(18) returns False, expected True.
Fix: return age >= 18

Line: 18
Problem: safe_ratio crashes when b is 0 due to division by zero.
Example: safe_ratio(5, 0) raises ZeroDivisionError, expected 0.
Fix: return a / b if b != 0 else 0

Line: 23
Problem: last_item raises IndexError for empty lists instead of None.
Example: last_item([]) raises IndexError, expected None.
Fix: return items[-1] if items else None

Line: 3
Problem: API_TOKEN is hardcoded in source code instead of read from environment variables.
Example: verify_token("secret_token_999") returns True, expected False.
Fix: API_TOKEN = os.environ.get("API_TOKEN", "")
