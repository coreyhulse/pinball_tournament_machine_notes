#import time
import requests
import json
#import csv
import math
from datetime import datetime
import psycopg2
import re

## Global Variables

## Connection variables

import postgres_connection

## Run Variables

extract_timestamp = datetime.now()

conn = psycopg2.connect(database=postgres_connection.database,
                        user=postgres_connection.user,
                        password=postgres_connection.password,
                        host=postgres_connection.host,
                        port=postgres_connection.port)

# creating a cursor object
cursor = conn.cursor()

print("---")
print("Conversion Starting!")
print("---")

sql_build = 'select machine_groups.*, opdb_group.opdb_group_id from sandbox.machine_groups left join sandbox.opdb_group on machine_groups.machine_group_id = opdb_group.machine_group_id where deleted_at is not null'

cursor.execute(sql_build)
print("Selecting rows from mobile table using cursor.fetchall")
machine_records = cursor.fetchall() 
   
for row in machine_records:

    machine_group_id = row[0]
    machine_name = row[1]
    machine_name_clean = re.sub(r'[^a-zA-Z0-9]','',machine_name)
    competition_setup = bytes(str(row[6]), "utf-8").decode("unicode_escape")
    competition_notes = bytes(str(row[7]), "utf-8").decode("unicode_escape")
    opdb_id = row[11]

    filename_cs = machine_name_clean + '_cs_' + machine_group_id + '_' +  opdb_id
    fileloc_cs = 'machines/' + filename_cs

    filename_cn = machine_name_clean + '_cn_' + machine_group_id + '_' +  opdb_id
    fileloc_cn = 'machines/' + filename_cn

    print("Id = ", row[0], " Machine = ", machine_name_clean)

    with open(fileloc_cs , 'w', encoding='UTF8', newline='\n') as f:

        f.write(str(competition_setup) + '\n')

    with open(fileloc_cn , 'w', encoding='UTF8', newline='\n') as f:

        f.write(str(competition_notes) + '\n')