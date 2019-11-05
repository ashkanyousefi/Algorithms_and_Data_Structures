# The following function will give the division and the remainder 

def divide_func(m,n):
    Remainder=m%n
    Factor= (m-Remainder)/n
    return Remainder,Factor

def coin_count(number_main):
    Remainder_10,Factor_10=divide_func(number_main,10)
    Remainder_5,Factor_5=divide_func(Remainder_10,5)
    return Factor_10,Factor_5,Remainder_5

# The main body of the program

number_main=Input_Digit=input("Enter the number: ")
coin_10,coin_5,coin_1=coin_count(number_main)

print("Number of coin 10 %d \n number of coin 5 %d \n number of coin 1 %d"%(coin_10,coin_5,coin_1))







