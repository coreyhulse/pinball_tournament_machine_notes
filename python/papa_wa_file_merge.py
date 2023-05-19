import os

# create a dictionary with file names as keys
# and for each file name the paths where they
# were found
file_paths = {}
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.md'):
            if f not in file_paths:
                file_paths[f] = []
            file_paths[f].append(root)

# for each file in the dictionary, concatenate
# the content of the files in each directory
# and write the merged content into a file
# with the same name at the top directory
for f, paths in file_paths.items():
    txt = []
    for p in paths:
        with open(os.path.join(p, f)) as f2:
            txt.append(f2.read())
    with open(f, 'w') as f3:
        f3.write(''.join(txt))