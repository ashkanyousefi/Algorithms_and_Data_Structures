
### Task4
The O(3n) as the program needs to go through 3 loops. I think there is a room to gain more efficieny by combining the loops. However the same comment as the Task3 will apply as the code will become more messy and complex to understand by combining the loops.


```python
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
Telemarketers=[]

for row in calls:
    Received_calls.append(row[1])
    if row[0][0:3]=='140':
        Possible_Telemarketers.append(row[0])

# for each in Possible_Telemarketers:
for row in texts:
    if row[1][0:3]=='140':
        Received_Texts.append(row[1])

for each in Possible_Telemarketers:
    if each not in (Received_calls or Received_Texts):
        if each not in Telemarketers:
            Telemarketers.append(each)
            
print("These numbers could be telemarketers:\n")  
Telemarketers.sort()
for each in Telemarketers:
    print("\n {0}".format(each))


```
