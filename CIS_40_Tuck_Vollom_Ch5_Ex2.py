'''
Tuck Vollom
This program calculates the pay of the employee.
It has capabilities of:
1) Calculate pay including overtime
2) Give the user a unique ID number for records
'''
from random import randint

OVERTIME_RATE = 1.5
REGULAR_HOURS = 40
overtime = 0
overtime_pay = 0
total_pay = 0



def main():
    the_hours, the_rate, company_name = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay, the_hours, the_rate, company_name)

def get_input():

    company_name = input('Enter your company name: ')

    flag = True
    while flag:
        try:

            hours = float(input('Enter hours worked: '))

            if hours > 0:
                flag = False
            else:
                print('The hours should be greater than zero, try again')

        except:
            print('Error, please enter numeric input')

    flag2 = True
    while  flag2:
        try:
            rate = float(input('Enter the rate: '))

            if rate > 0:
                flag2 = False
            else:
                print('The rate should be greater than zero, try again')
        except:
            print('Error, please enter numeric input')



    return hours, rate, company_name

def compute_pay(the_hours, the_rate):   
    if the_hours > REGULAR_HOURS:
        overtime = the_hours - REGULAR_HOURS
        overtime_pay = overtime * the_rate *OVERTIME_RATE
        total_pay = REGULAR_HOURS * the_rate + overtime_pay
    else:
        total_pay = the_hours * the_rate
    return total_pay

def print_output(the_pay, the_hours, the_rate, company_name):
    #Output values entered by user
    print('Company:', company_name)
    print('hours:', the_hours)
    print('Rate:', the_rate)
    print('**********************************************')
    print('Your document numer is: ',randint(1000, 2000))
    print('Your', company_name, 'gross pay is', the_pay, 'dollars.')

main()


'''
Test1:
Enter your company name: Google
Enter hours worked: 40
Enter the rate: 10
Company: Google
hours: 40.0
Rate: 10.0
**********************************************
Your document numer is:  1016
Your Google gross pay is 400.0 dollars.

Test2
Enter your company name: Amazon
Enter hours worked: 45
Enter the rate: 120
Company: Amazon
hours: 45.0
Rate: 120.0
**********************************************
Your document numer is:  1191
Your Amazon gross pay is 5700.0 dollars.

Test3
Enter your company name: Facebook
Enter hours worked: 60
Enter the rate: 99
Company: Facebook
hours: 60.0
Rate: 99.0
**********************************************
Your document numer is:  1780
Your Facebook gross pay is 6930.0 dollars.

'''
