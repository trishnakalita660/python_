import re

text_to_search = '''
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
'''

sentence = 'Start a sentence and then bring it to an end'

#  '.' matches with all characters except new line. there are many esc characters.

pattern = re.compile(r'coreyms\.com') # seperates pattern into reusable variable

matches = pattern.finditer(text_to_search) #gathers all the matches in easy-to-read format

for match in matches:
    print(match)


#  matching phone number in the multiline string
#  using meta characters

ptrn_number = re.compile(r'[89]00.\d\d\d.\d\d\d')

ptrn_match = ptrn_number.finditer(text_to_search)


for match in ptrn_match:
    print(match)



#  parse phone numbers from dummyData

pattern_num = re.compile(r'\d{3}[-.]\d\{3}[-.]\d{3}')  # matches only 000{.or-}000{.or-}000 (character set)

with open('dummyData.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    matches = pattern_num.finditer(contents)

    for match in matches:
        print(match)


#  return anything but not 'bat'

text = '''cat mat rat bat'''

pat = re.compile(r'[^b]at')
mat = pat.finditer(text)

for m in mat:
    print(m)


#  match more than one character at once
#  QUANTIFIERS

ptrn = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') 

ptrn_match = ptrn.finditer(text_to_search)


for match in ptrn_match:
    print(match)

# other methods 
# findall returns list of tuples of the!
#  match checks if the reg ex matches at the beginning of the string
# search method