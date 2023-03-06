#Tan Hyong Hsing
#20DDT21F1002

car_price = 90000
minimum_dp = 0.10 * car_price
fixed_interest_rate = 0.027


customer_dp = int(input('Please enter your downpayment: '))

if customer_dp < minimum_dp :
    print('You are not eligible for the bank loan.')
else :
    loan_amount = car_price - customer_dp
    loan = int(input('How long you want to make a loan in years(1 to 9 years only): '))
    total_interest = fixed_interest_rate * loan_amount  * loan
    loan_period_in_month = loan * 12
    monthly_installment = (loan_amount + total_interest) / loan_period_in_month
    two_decimal = round(monthly_installment ,2)
    print('You need to pay RM ' + str(two_decimal) + ' monthly as your monthly payment.')