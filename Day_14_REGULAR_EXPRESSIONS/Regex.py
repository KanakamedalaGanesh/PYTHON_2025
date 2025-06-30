'''Regular Expressions: Regex is a powerful tool for matching patterns in strings.It allows you to search, match, and manipulate strings based on specific patterns.
The basic syntax of regex includes:
1. Literal characters: Match the exact characters in the string.
2. Metacharacters: Special characters that have a specific meaning in regex, such as . (dot), * (asterisk), + (plus), ? (question mark), ^ (caret), $ (dollar sign), [] (square brackets), {} (curly braces), () (parentheses), | (pipe).
3. Character classes: Define a set of characters to match, such as [a-z] (any lowercase letter), [A-Z] (any uppercase letter), [0-9] (any digit), and [^abc] (any character except a, b, or c).
4. Quantifiers: Specify how many times a character or group of characters should appear, such as * (zero or more), + (one or more), ? (zero or one), {n} (exactly n times), {n,} (at least n times), {n,m} (between n and m times).
5. Anchors: Specify the position of a match in the string, such as ^ (start of the string) and $ (end of the string).
6. Groups: Allow you to group characters or patterns together, such as (abc) (match the exact sequence "abc") and (a|b|c) (match either "a", "b", or "c").
7. Escape sequences: Use a backslash \ to escape special characters, such as \. (match a literal dot) or \d (match any digit).
8. Flags: Modify the behavior of regex, such as re.IGNORECASE (case-insensitive matching) or re.MULTILINE (match across multiple lines).
9. Lookahead and lookbehind assertions: Allow you to match a pattern only if it is followed or preceded by another pattern, such as (?=abc) (lookahead for "abc") or (?<=abc) (lookbehind for "abc").
10. Non-capturing groups: Use (?:...) to group patterns without capturing them for backreferences.
# Regular expressions are used in various applications, such as data validation, text processing, and web scraping.
'''
import re
# Example of using regex to find all email addresses in a string
text = "Please contact us at john.doe@example.com or jane.doe@example.com for more information."


# Regular expression pattern to match email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


# Find all matches of the pattern in the text
matches = re.findall(pattern, text)


# Print the matched email addresses
for match in matches:
    print(match)


# Example of using regex to validate a phone number
phone_number = "123-456-7890"


# Regular expression pattern to match a phone number in the format XXX-XXX-XXXX
pattern_phone = r'^\d{3}-\d{3}-\d{4}$'


# Validate the phone number using the pattern
if re.match(pattern_phone, phone_number):
    print(f"{phone_number} is a valid phone number.")
else:
    print(f"{phone_number} is not a valid phone number.")


# Example of using regex to replace all occurrences of a word in a string
text_to_replace = "The quick brown fox jumps over the lazy dog."
replacement_pattern = r'\bfox\b'
replacement_text = "cat"


# Replace all occurrences of the word "fox" with "cat"
replaced_text = re.sub(replacement_pattern, replacement_text, text_to_replace)
print(replaced_text)  # Output: The quick brown cat jumps over the lazy dog.


# Example of using regex to split a string by whitespace
split_text = "This is a sample text with multiple spaces."


# Regular expression pattern to match one or more whitespace characters
split_pattern = r'\s+'


# Split the text using the pattern
split_result = re.split(split_pattern, split_text)
print(split_result)  # Output: ['This', 'is', 'a', 'sample', 'text', 'with', 'multiple', 'spaces.']


# Example of using regex to find all words in a string
word_text = "Hello, world! This is a test."


# Regular expression pattern to match words (alphanumeric characters)
word_pattern = r'\b\w+\b'


# Find all words in the text
word_matches = re.findall(word_pattern, word_text)
print(word_matches)  # Output: ['Hello', 'world', 'This', 'is', 'a', 'test']


# Example of using regex to validate a URL
url = "https://www.example.com"


# Regular expression pattern to match a URL
url_pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'


# Validate the URL using the pattern
if re.match(url_pattern, url):
    print(f"{url} is a valid URL.")
else:
    print(f"{url} is not a valid URL.")


# Example of using regex to extract dates from a string
date_text = "The event will be held on 2023-10-15 and 2023-11-20."


# Regular expression pattern to match dates in the format YYYY-MM-DD
date_pattern = r'\d{4}-\d{2}-\d{2}'


# Find all dates in the text
date_matches = re.findall(date_pattern, date_text)
print(date_matches)  # Output: ['2023-10-15', '2023-11-20']
