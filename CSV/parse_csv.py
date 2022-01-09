# Read, Parse, and Write CSV Files

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('parsed_names.csv', 'w') as new_file:
        fieldname = ['first_name', 'last_name', 'email']
   
        csv_write = csv.DictWriter(new_file,fieldnames=fieldname, delimiter = '\t')
        csv_write.writeheader()

        for line in csv_reader: 
            csv_write.writerow(line)

# with open('parsed_names.csv', 'r') as open_fil:
#      csv_open = csv.DictReader(open_fil, delimiter='\t')

#     for line in csv_open:
#         print(line['email']) 