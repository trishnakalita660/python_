import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

# for match in matches:
#     print(match)


#  get only domain names
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

url_pat = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

url_matches = url_pat.finditer(urls)
sub_url = url_pat.sub(r'\2\3', urls)
print(sub_url)
for url in url_matches:
    print(url.group(1))

