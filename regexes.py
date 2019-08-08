import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
sat
"""

sentence = "Start a sentence and then bring it to an end"

emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# pattern = re.compile(r"abc")
# pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
# pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")
# pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")
# pattern = re.compile(r"[^b]at")
# pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
# pattern = re.compile(r"Mr\.?\s[A-Z]\w*")
# pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")
# pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")
# pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
# pattern = re.compile(r"https?://(www\.)?\w+\.\w+")
# pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
pattern = re.compile(r"start", re.IGNORECASE)
# pattern = re.compile(r"")

# subbed_urls = pattern.sub(r"\2\3", urls)
# print(subbed_urls)

matches = pattern.finditer(sentence)
# matches = pattern.finditer(emails)
# matches = pattern.finditer(urls)
# matches = pattern.findall(text_to_search)

for match in matches:
    print(match)
#     print(match.group(3))

# print(text_to_search[1:4])


# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


# #### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

