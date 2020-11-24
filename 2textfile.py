"""import difflib
with open('diffFile1.txt', 'r') as file1 :
    with open('C:\\Users\\swat\\Documents\\NationalGrid\\oc2_env\\oc2_codes\\diffFile2.txt', 'r') as file2 :
        for line in difflib.unified_diff(file1, file2, fromfile='diffFile1.txt', tofile='diffFile2.txt', lineterm=''):
            print(line)

            #C:\\Users\\swat\\Documents\\NationalGrid\\oc2_env\\oc2_codes\\"""

import difflib
with open('diffFile1.txt') as f1:
    f1_text = f1.read()
with open('diffFile2.txt') as f2:
    f2_text = f2.read()
# Find and print the diff:
for line in difflib.unified_diff(f1_text, f2_text, fromfile='file1', tofile='file2', lineterm=''):
    print(line)