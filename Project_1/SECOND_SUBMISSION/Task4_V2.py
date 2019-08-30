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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

Possible_Telemarketers=[]
Received_calls=[]
Received_Texts=[]
Sent_Texts=[]
Telemarketers=set()

for row in calls:
    Received_calls.append(row[1])
    Possible_Telemarketers.append(row[0])

# for each in Possible_Telemarketers:
for row in texts:
    Sent_Texts.append(row[0])
    Received_Texts.append(row[1])

for each in Possible_Telemarketers:
    if each not in (Received_calls or Received_Texts or Sent_Texts or Received_Texts):
            Telemarketers.add(each)

Final_List=sorted(Telemarketers)
print("These numbers could be telemarketers:\n")  
print(*Final_List,sep='\n')