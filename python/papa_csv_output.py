import csv
import re

file = open('python/OPDB_Group_PAPA.csv', encoding='utf-8')

type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []
for row in csvreader:
    rows.append(row)
    opdb_name = row[0]
    opdb_name_clean = re.sub(r'[^a-zA-Z0-9]','',opdb_name)
    machine_settings = row[4]
    tech_notes = row[5]
    concerns = row[6]
    lock_stealing = row[7]
    opdb_id = row[8]

    if str(machine_settings) != '':

        competition_setup = ''

        competition_setup = competition_setup + '''***
The following was imported from the PAPA/ReplayFX Competition Notes webpage at https://replayfoundation.org/papa/learning-center/director-guide/game-notes/#GameNotes

'''

        competition_setup = competition_setup + machine_settings
    else:

        competition_setup = ''

    competition_file = open('machine_papa/' + opdb_name_clean + '_cs_' + opdb_id + '.md', 'w')

    competition_file.write(competition_setup)

    competition_file.close

    print(opdb_name_clean + " cs notes created")

    if str(tech_notes) != '' or str(concerns) != '':

        competition_notes = ''

        competition_notes = competition_notes + '''***
The following was imported from the PAPA/ReplayFX Competition Notes webpage at https://replayfoundation.org/papa/learning-center/director-guide/game-notes/#GameNotes

'''

        if str(tech_notes) != '':
        
            competition_notes = competition_notes + '''### Tech Notes
            
''' + tech_notes

        if str(concerns) != '':
        
            competition_notes = competition_notes + '''### Concerns
            
''' + concerns
        
    else: 

        competition_notes = ''

    competition_file = open('machine_papa/' + opdb_name_clean + '_cn_' + opdb_id + '.md', 'w')

    competition_file.write(competition_notes)
        
    competition_file.close
        
    print(opdb_name_clean + " cn notes created")




rows

file.close()

