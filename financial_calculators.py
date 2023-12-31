import math

#The following program is to calculate the amount of interest earned on an investment, or the amount that needs to be paid on a home loan


intro = '''
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan'''

print(intro)
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
user_input = user_input.lower()

if user_input == "investment":
    deposit_amount = int(input("Enter the amount of money deposited:"))
    interest_rate_investment = (float(input("Enter the interest rate without including the percentage sign (%):"))/100)
    investment_years = int(input("Enter the number of years for which you plan to invest:"))
    interest = input("Enter either 'simple' or 'compound', depending on the desired interest type:")
    interest = interest.lower()

    if interest == "simple":
        investment_simple_interest = deposit_amount*(1 + (interest_rate_investment*investment_years))

        investment_simple_calculation = f'''

        Investment Interest Calculation

        Amount deposited:                       {deposit_amount}
        Interest Rate:                          {interest_rate_investment}
        Length of Investment:                   {investment_years}
        Type of Interest:                       {interest}

        Total Amount with Interest:             {investment_simple_interest}
        '''

        print(investment_simple_calculation)

    elif interest == "compound":
        investment_compound_interest = deposit_amount*(math.pow((1 + interest_rate_investment), investment_years))
       
        investment_compound_calculation = f'''

        Investment Interest Calculation

        Amount deposited:                       {deposit_amount}
        Interest Rate:                          {interest_rate_investment}
        Length of Investment:                   {investment_years}
        Type of Interest:                       {interest}

        Total Amount with Interest:             {investment_compound_interest}
        '''

        print(investment_compound_calculation)
    
    else:
        print("ERROR: There seems to have been an issue with the values you've input. Kindly try again, reading the prompts carefully.")
elif user_input == "bond":
    house_value = float(input("Enter the present value of the house:"))
    interest_rate_bond = (int(input("Enter the interest rate without including the percentage sign (%):"))/100)
    repayment_time = int(input("Enter the amount of months over which you would like to repay the bond:"))

    bond_monthly_repayment = (((interest_rate_bond / 12) * house_value)/((1 - ((1 + (interest_rate_bond/12))**(-1 * repayment_time)))))

    bond_repayment_calculation = f'''

        Bond Repayment Calculation

        Present Value of House:              {house_value}
        Interest Rate:                       {interest_rate_bond}
        Repayment Period (In Months):        {repayment_time}

        Total Amount to be Paid Monthly:     {bond_monthly_repayment}
        '''
    print(bond_repayment_calculation)
else: 
    print("ERROR: There seems to have been an issue with the values you've input. Kindly try again, reading the prompts carefully.")