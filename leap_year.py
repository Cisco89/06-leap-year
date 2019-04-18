# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence

def is_leap_year(year):
    the_year_is_leap = False
    if year % 4 == 0:
        the_year_is_leap = True
    if year % 100 == 0:
        the_year_is_leap = False
    if year % 400 == 0:
        the_year_is_leap = True
    return the_year_is_leap
