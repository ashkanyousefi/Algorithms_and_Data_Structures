

```python
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import operator
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
Phone_Call_Duration=defaultdict(lambda:0)

for row in calls:
    Phone_Call_Duration[row[0]]+=int(row[3])
    Phone_Call_Duration[row[1]]+=int(row[3])
    
Max_finder=[(value,key) for key,value in Phone_Call_Duration.items()]
print(max(Max_finder)[1])



```
