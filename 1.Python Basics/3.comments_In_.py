## What is comment?

"""
In Python, comments are used to explain code and are ignored by the interpreter during execution. There are three types of comments in Python:

Single-line comments: These are created using the hash symbol (#). Everything after the # on that line is considered a comment.
python
Copy code
# This is a single-line comment
print("Hello, World!")  # This is an inline comment
Multi-line comments using multiple hashes: You can create multi-line comments by using a hash symbol at the beginning of each line.
python
Copy code
# This is a multi-line
# comment in Python
print("Hello, World!")
Multi-line comments using string literals: Since Python ignores string literals that are not assigned to a variable, we can use these string literals as comments. This is particularly useful when you want to add a block of comments that spans multiple lines.
python
Copy code
"""
# This is a multi-line
# comment in Python
"""
print("Hello, World!")
When to use comments in Python:

To explain the purpose of a section of code.
To explain why a particular approach was chosen.
To temporarily disable a part of the code during debugging.
To comment out code that is no longer needed but should be preserved for future reference.

"""

# Single line
print("This is a single line comment.")
# Multi-line
print(
    "This is the first line of a multi-line\n",
    "comment.\n",
    "And this is another line."
)

"""
    This is also multiline comments
"""