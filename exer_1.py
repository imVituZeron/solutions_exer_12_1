# --------------------------------------------------------------------#
# Email:         vitorpaulasantos@gmail.com
# Author:        Vitor de Paula Santos
# Maintenance:   Vitor de Paula Santos
# --------------------------------------------------------------------#
# ChangeLog:
#  
#    v1.0 20/07/2021, Vitor Santos
# --------------------------------------------------------------------#

# ----------------------- Functions ---------------------------------#
def return_values(list):
    bigger = max(list)
    the_sum = sum(list)
    primary = list[0]
    media = sum(list)/len(list)
    negative = 0

    for i in list:
        if i < 0:
            negative +=i

    print(f"""
    BIGGER: {bigger}
    THE SUM: {the_sum}
    PRIMARY: {primary}
    MEDIA: {media}
    NEGATIVE SUM: {negative}
    """)
# ----------------------------------------------------------------------#

# -------------------------------- MAIN --------------------------------#
list_numbers = []
while True:
    numbers = int(input("Insert a digit: "))
    op = input("Do you want insert more? [Y/N]")
    list_numbers.append(numbers)

    if op.isnumeric():
        print("please, inform correctly!")
    elif op.isalpha() and op == "Y":
        print("See you next time!")
        break
    
return_values(list_numbers)
# -----------------------------------------------------------------------#
