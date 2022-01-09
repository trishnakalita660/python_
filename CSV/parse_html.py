import csv

html_op = ''
names= []

with open ('data.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file) # DictReader= stores as key value pair
    
    
    ''' header and first line removal'''
    next(csv_data)
    
    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

print(names)

html_op+= f'<p> There a {len(names)} people </p>'

html_op += '\n<ul>'

for name in names:
    html_op+= f'\n <li>{name}</li>'

html_op+= '\n</ul>'

print(html_op)