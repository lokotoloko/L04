import os

API_TOKEN = os.environ.get("API_TOKEN", "")

def is_even(n):
    """True if n is an even number"""
    return n % 2 == 0

def can_vote(age):
    """True if age is 18 or older"""
    return age >= 18

def safe_ratio(a, b):
    """a divided by b, or 0 if b is 0"""
    return a / b if b != 0 else 0

def last_item(items):
    """The last item of a list, or None if the list is empty"""
    return items[-1] if items else None

def verify_token(token):
    """True if token matches the environment API_TOKEN (when set)"""
    return API_TOKEN != "" and token == API_TOKEN
