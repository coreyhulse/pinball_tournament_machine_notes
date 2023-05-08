import os
import re

directory = 'machine_wa'
 
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():

        print(filename)
    
        modified_contents = open(filename, 'r+', encoding='utf-8')

        read_file = modified_contents.read()

        data_buffer = ''

        data_buffer =  '''***
The following was imported from the WA Pinball Machine Notes webpage at http://wapinball.net/setups/

''' + read_file
                
        #print(data_buffer)

        removed_lines = ''

 #       for line in data_buffer:
 #           if not line.isspace():
 #               removed_lines = removed_lines + line + '\r\n'

        removed_lines = re.sub(r'^$\n', '', data_buffer, flags=re.MULTILINE)

        modified_contents.close

        file_replacement = open(filename, 'w', encoding='utf-8')

        file_replacement.write(removed_lines)

        file_replacement.close

        #print(removed_lines)

        # modified_contents.write(removed_lines)
        

#         filename.write(read_file)
        
#         filename.close




