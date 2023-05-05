import csv
import re
import pandoc
import pypandoc


file = open('python/wapinball_mapping.csv', encoding='utf-8')

type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
    rows.append(row)

    file_name = row[1]
    opdb_name = row[6]
    opdb_name_clean = re.sub(r'[^a-zA-Z0-9]','',opdb_name)
    opdb_id = row[7]


    pypandoc.convert_file("docx/" + file_name, 'md', outputfile="machine_wa/" + opdb_name_clean + "_cn_" + opdb_id + ".md", extra_args=('--standalone','--wrap=none'))
    
    print(opdb_name_clean + 'wa_pinball notes created')


rows

file.close()