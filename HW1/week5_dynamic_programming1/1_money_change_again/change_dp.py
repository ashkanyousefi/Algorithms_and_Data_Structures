# Uses python3
# import sys

# def get_change(m):
#     #write your code here
#     return m // 4

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))


#The solution could be implemented by considering all the possibilities for the coin combinations 
#Then the we need to remove all the combinations that exceed the possible sumation
#In the next step, we will pick the solution which leads to the minimum possible results.

import itertools
available_coins=[2,3,5,10]
money_change=80

# available_coins=int(input('Enter the array which is a list of available coins:'))
# money_change=input('Enter the value to receive your change:')

def money_exchange(available_coins,money_change):
    total_combinations=[]
    final_answer={}
    for i in range(2,len(available_coins)):
        total_combinations.append(itertools.combinations(available_coins,i))

    for item in total_combinations:
        for each in item:
            if sum(each)==money_change:
                final_answer[len(each)]=each
    return final_answer

if __name__ == "__main__":
    print(money_exchange(available_coins,money_change))

#This problem can be extended by calculating the combination values and then divide the money change to 
# the combination value to get the exact number of coins needed. 