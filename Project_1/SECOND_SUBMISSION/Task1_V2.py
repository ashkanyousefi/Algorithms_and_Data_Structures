"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

Full_List=[]
for row in calls:
    Full_List.append(row[0])
    Full_List.append(row[1])
for row in texts[1:]:
    Full_List.append(row[0])
    Full_List.append(row[1])
Full_List_Unique=len(set(Full_List))

print('There are {0} different telephone numbers in the records'.format(Full_List_Unique))