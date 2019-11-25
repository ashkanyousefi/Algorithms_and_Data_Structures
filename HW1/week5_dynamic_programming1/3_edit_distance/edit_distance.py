
# def edit_distance(first_string,second_string):
#     register=[]
#     longest_length=max(len(first_string),len(second_string))
#     for sh in range(-2,2):
#         count=0
#         for i in range(sh,sh+longest_length):
#             if first_string[i] != second_string[i]:
#                 count+=1
#         register.append((sh,count))
#     result=[sum(abs(sh)+count)]
#     return min(result)

# first_string=input('Enter the first string: ')
# second_string=input('Enter the second string: ')

# if __name__ == "__main__":
#     print(edit_distance(first_string,second_string)
    
string1 = "#short"
string2 = "#ports"


my_results=[[(0,0)] * len(string1) for _ in range(len(string2))]
my_array=[[0] * len(string1) for _ in range(len(string2))]

for i in range(len(string2)):
    my_array[i][0] = i

for j in range(len(string1)):
    my_array[0][j] = j

for i in range(1,len(string2)):
    for j in range(1,len(string1)):
        if string1[j]==string2[i]:
            c1=0+my_array[i-1][j-1]
        else:
            c1=1+my_array[i-1][j-1]

        c2=1+my_array[i-1][j]
        c3=1+my_array[i][j-1]
        my_array[i][j]=min(c1,c2,c3)
        
        ar=min(c1,c2,c3)
        if ar==c1:
            register_results=(-1,-1)
        if ar==c2:
            register_results=(-1,0)
        if ar==c3:
            register_results=(0,-1)
        my_results[i][j]=register_results


def my_print(arr):
    print("\n".join([" ".join(map(str, row)) for row in arr]))

my_print(my_array)
my_print(my_results)



