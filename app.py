# 1. As a valued customer at the Bank of Honolulu, you make a deposit of $1000. Your savings account balance prior to the deposit has an amount of $8000. Calculate the new savings account balance. Print the new savings account balance and concatenate the dollar sign.
balance = 8000
deposit = 1000
balance = balance + deposit
print("$"+str(balance))
# 2.You need to pay taxes on the $500 cash prize that you won to the IRS ( The tax rate is 30%). Calculate the tax amount and subtract this from your savings balance. Print the updated savings account balance and concatenate the dollar sign.
prize = 500
tax_rate = 0.30
balance = balance - (prize*tax_rate)
print("$" + str(balance))
# 3. The savings account accrues an annual interest rate of 2%. Calculate the interest earned for the first quarter of 2018, using the original account balance from Question 1. Print the interst earned in the first quarter and concatenate the dollar sign.
interest_rate = 0.005 #per quarter
balance = interest_rate * balance + balance
print("$"+ str(balance))


# 4. Function add
# Create a function that will take two parameters named num1 and num2. This function will add two numbers. Print your result.
def add(num1, num2):
    sum=num1+num2
    return sum

this=add(2,3)
print(this)
    
# 5. Function subtract
# Create a function that will take two parameters named num1 and num2. This function will subtract two numbers. Print your result.
def subtract(num1,num2):
    difference=num1-num2
    return difference

this=subtract(5,3)
print(this)


# 6. Function add-then-subtract
# Create a function that will take in three parameters named num1, num2 and num3. The function will sum up the first two parameters (num1 and num2) and subtract it from the third parameter (num3). Please use your previous functions (i.e. add or subtract) for this exercise. Print your result.
def add_then_sub(num1,num2,num3):
    sum=num1+num2
    difference=num3-sum
    return difference

this=add_then_sub(3,5,20)
print(this)



# 7. Function shoe size
#  Create a function that will take in a parameter named inches. This function will convert inches to centimeters(cm). Print your result. 
def shoe_size(inches):
    cent=inches*2.54
    return cent

this=shoe_size(12)
print(this)


# 8. Create a function that will take in a parameter named cel. The function will convert Celsius into Fahrenheit. Print your result.
def temp(cel):
    far=cel*(9/5)+32
    return far
this=temp(-40)
print(this)
# 9. Function all caps
#  Create a function that will take in a parameter named str. This function will capitalize all the letters in the string. Print your result. 
def cap(str):
    caps=str.upper()
    return caps

this=cap("hello world")
print(this)

# 10. Function one cap
#  Create a function that will take in a parameter named str. The function will capitalize only the first letter in the string. Print your result.
def cap_first(str):
    capf=str.title()
    return capf

this=cap_first("hello world")
print(this)
# 11. Use the extend method to combine the following lists together. Print your result.

east_side = ['Biggie', 'Nas', 'Wu-Tang Clan']
west_side = ['Tupac', 'Dre', 'Snoop']
east_side.extend(west_side)
print(east_side)
# 12. Use the clear method to remove all items from the following list. If you are using Python 2 or 3.2, use the del operator instead. Print your result.

haters = ['Keyshia Cole', 'Wendy Williams', '50 Cent', 'Lil Kim']
haters.clear()
print(haters)












