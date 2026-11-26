# Bug reports for exercise4.py

Line: 4
Problem: ADMIN_PASSWORD is hardcoded in source code, exposing it to potential exposure and making it easy to guess or compromise.
Example: check_admin("admin123") returns True, expected False.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")

Line: 14
Problem: SQL query uses string formatting without parameterization, allowing SQL injection attacks.
Example: find_user(db, "' OR '1'='1") returns a user row, expected None.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
