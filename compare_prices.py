""" Create a script that take a month price, an annual price and time of use, and tell you if the deal is a good deal or not"""

from datetime import date
from dateutil.relativedelta import relativedelta


def final_time(number_months):
    """Calculate and returns an especific date, acording with the number of months than receive as parameter"""

    months = date.today() + relativedelta(months=+number_months)
    return months

def compare_prices(month, annual, time):
    """Given a price by month, annual and and amount of time in months, determine if a deal is good or not"""

    full_month = month * 12
    full_annual = annual * 12
    full_use = month * time

    if full_use < full_annual:
        saving = full_annual - full_use
        saving_months = saving / annual
        print "Buy it by month. You're using %i and saving %i months" % (time, saving_months)
    else:
        saving = full_use - full_annual
        saving_months = saving / month 
        print "Buy it by annual. You're using %i and saving %i months" % (time, saving_months)

if __name__ == "__main__":

    compare_prices(19, 15.75, 6)
    print "$$$$$$$$$$$"
    compare_prices(19, 15.75, 10)
    print "$$$$$$$$$$$"
    compare_prices(19, 15.75, 12)
    print "$$$$$$$$$$$"
    compare_prices(19, 15.75, 4)
