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

Quantifiers:
*   `*` matches zero or more occurrences of the preceding element.
*   `+` matches one or more occurrences of the preceding element.
*   `?` matches zero or one occurrence of the preceding element.
*   `{n}` matches exactly n occurrences of the preceding element.
*   `{n,}` matches at least n occurrences of the preceding element.
*   `{n,m}` matches between n and m occurrences of the preceding element.


Regex methods : 
1. `re.search()`: Searches for the first occurrence of the pattern in the string.
2. `re.match()`: Searches for the pattern at the beginning of the string.                         *
3. `re.fullmatch()`: Searches for the pattern that matches the entire string.                     *
4. `re.findall()`: Finds all occurrences of the pattern in the string and returns them as a list. *
5. `re.finditer()`: Finds all occurrences of the pattern in the string and returns them as an iterator.
6. `re.split()`: Splits the string into substrings based on the pattern.                          *
7. `re.sub()`: Replaces occurrences of the pattern in the string with a replacement string .
8. `re.subn()`: Replaces occurrences of the pattern in the string with a replacement string and returns the number of replacements made.


Special Characters:
*   `.` matches any single character.
*   `^` matches the start of the string.
*   `$` matches the end of the string.
*   `|` is a logical OR operator.
*   `[]` defines a character class.
*   `()` defines a group.
*   `*` is a quantifier that matches zero or more occurrences of the preceding element.
*   `+` is a quantifier that matches one or more occurrences of the preceding element.
*   `?` is a quantifier that matches zero or one occurrence of the preceding element.
*   `{n}` is a quantifier that matches exactly n occurrences of the preceding element.
*   `{n,}` is a quantifier that matches at least n occurrences of the preceding element.
*   `{n,m}` is a quantifier that matches between n and m occurrences of the preceding element.

Example:
print( re.search(r'\d+', 'abc123def456').group() ) # Output: 123
print( re.search(r'\d+', 'abc123def456').group(0) ) # Output: 123



Sequence:
1. \d matches any digit.
2. \D matches any non-digit.
3. \s matches any whitespace character.
4. \S matches any non-whitespace character.
5. \w matches any alphanumeric character.
6. \W matches any non-alphanumeric character.
7. \b matches a word boundary.
8. \B matches a non-word boundary.
9. \A matches the start of the string.
10. \Z matches the end of the string.
11. \G matches the position where the previous match ended.
12. \m matches the start of the string.
13. \M matches the start of the string.
14. \n matches the newline character.
15. \r matches the carriage return character.
16. \t matches the tab character.
17. \v matches the vertical tab character.
18. \0 matches the null character.
19. \x matches a hexadecimal escape sequence.
20. \u matches a Unicode escape sequence.
21. \U matches a Unicode escape sequence.
22. \N{...} matches a Unicode character by name.

Example:
print( re.findall(r'\d+', 'abc123def456') )  # Output: ['123', '456']
print( re.findall(r'\d+', 'abc123def456', re.IGNORECASE) ) # Output: ['123', '456']
print( re.findall(r'\d+', 'abc123def456', re.MULTILINE) ) # Output: ['123', '456']
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
