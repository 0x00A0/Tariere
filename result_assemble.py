# read all csv files in ./flags/ and assemble them into a single file flags.csv, with 3 colomns: image_name, flag_name, flag_value

import csv
import os

flags = []
for filename in os.listdir('flags'):
    with open(f'flags/{filename}', mode='r') as file:
        reader = csv.reader(file, delimiter=' ')
        _flags=list(reader)
        if _flags == []:
            continue
        for row in _flags:
            if row==[]:
                continue
            flags.append(['.'.join(filename.split('.')[:-1]), row[0], row[1]])
            
with open('flags.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(flags)
    
print(f"Flags assembled in flags.csv")

