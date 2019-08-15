
### Task1
* The efficiency level for the Task1 is again O(1).
* Same comment as the task 0 and I just used the basic Python comments to solve the problem.


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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

Total=(len(calls)+len(texts))*2
print('There are{0:6d} different telephone numbers in the records'.format(Total))
```
