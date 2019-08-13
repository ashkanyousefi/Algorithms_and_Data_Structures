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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""



Area=[]
Mobile=[]

for row in calls:
    if row[0][0:5]=='(080)' and row[1][0]=='(':
        Place_Holder=(row[1].split(')'))[0]
        if Place_Holder[1:] not in Area:
            Area.append(Place_Holder[1:])
            
    if row[0][0:5]=='(080)' and row[1][0]=='7':
        Place_Holder=(row[1].split(' '))[0]
        if Place_Holder not in Mobile:
            Mobile.append(Place_Holder[0:4])
            
            
    if row[0][0:5]=='(080)' and row[1][0]=='8':
        Place_Holder=(row[1].split(' '))[0]
        if Place_Holder not in Mobile:
            Mobile.append(Place_Holder[0:4])
            
            
    if row[0][0:5]=='(080)' and row[1][0]=='9':
        Place_Holder=(row[1].split(' '))[0]
        if Place_Holder not in Mobile:
            Mobile.append(Place_Holder[0:4])

print(len(Area))
print(len(Mobile))

#Step 2

Banglore_received_calls=[]
Total_calls=[]

for row in calls:
    if row[0][0:5]=='(080)' and row[1][0:5]=='(080)':
        Place_Holder=row[1]
        Banglore_received_calls.append(Place_Holder)
        
    if row[0][0:5]=='(080)':
        Total_calls.append(row[1])

    
L_Banglore_received_calls=len(Banglore_received_calls)
L_Total_calls=len(Total_calls)
Percentage=(L_Banglore_received_calls/L_Total_calls)*100
print('The total percentage of the Banglore calls {0:3.3f}%'.format(Percentage))

