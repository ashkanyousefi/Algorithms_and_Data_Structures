# The following function will give the division and the remainder 

#%%
def divide_func(m,n):
    remainder=m%n
    factor= m//n
    return remainder,factor

#%%

def coin_count(number_main):
    Remainder_10,Factor_10=divide_func(number_main,10)
    Remainder_5,Factor_5=divide_func(Remainder_10,5)
    Remainder_1,Factor_1=divide_func(Remainder_5,1)

    return (Factor_10+Factor_5+Factor_1)


#%%
# The main body of the program

Input_Digit=int(input("Enter the number: "))
print(coin_count(Input_Digit))


# %%
