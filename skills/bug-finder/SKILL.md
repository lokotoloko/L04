---
name: bug-finder
description: Output bug reports in strict Line/Problem/Example/Fix format with zero markdown.
---

Find all 5 bugs in the Python file.
Your VERY FIRST WORD must be `Line:`. Do NOT write any intro, summary, numbers, bullets, bold (`**`), or code blocks (```).

Follow this EXACT 4-line template for each bug, separated by one blank line:

Line: <line number>
Problem: <short description>
Example: <function_call> returns <wrong>, expected <right>
Fix: <single line of Python code>

Example output:
Line: 8
Problem: is_even checks == 1 instead of == 0.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0
