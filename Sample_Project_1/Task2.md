
### Task2
The task 2 has a big O of 2n means that with the scaling of the input the runtime grows with 2n and I realized that with combination of two loops the run time could be reduced to n from 2n. There is a possibility to gain 100% efficiency can be gained.


```python
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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
Call_Duration=[row[3] for row in calls]
Max_Duration=max(Call_Duration)

for row in calls:
    if row[3]==Max_Duration:
        print('The longest time spent belongs to: \n phone number: {0} \n phone_number: {1}'.format(row[0],row[1]))

```


```python

```


```python

```