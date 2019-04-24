#
# ps7pr5.py (Problem Set 7, Problem 5)
#
# TT Securities
#
#  Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your TT investment plan')
    ## Add the new menu options here.

    print('(8) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    ## IMPORTANT: You will need to change this function so
    ## that it prints a table of days and prices.
    print('current prices:', prices)
    print('Day  Price')
    print('----------')
    day = 0 # day
    for val in prices:
        print(' ', day, '%7.2f'% val)
        day += 1

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your helper functions for options 3-7 below.
# a help function for (3) and (4)
def get_average(prices):
    sum_p = 0
    for val in prices:
        sum_p += val
    return sum_p/len(prices)
# (3)
def average_price(prices):
    print('current average price:%7.2f'% get_average(prices))
# (4)
def standard_deviation(prices):
    sum_deviation = 0
    for val in prices:
        sum_deviation += (val - get_average(prices))*(val - get_average(prices))
    deviation = sum_deviation/len(prices)
    print('current standard deviation:%7.2f'%deviation)
# (5)
def max_price(prices):
    max_p = prices[0]
    max_d = 0
    for day in range(len(prices)):
        if prices[day] > max_p:
            max_p = prices[day]
            max_d = day
    print('the current max price:')
    print('Day  Price')
    print('----------')
    print(' ', max_d, '%7.2f'% max_p)
# (6)
def threshould(prices):
    val_thr = int(input('Enter your threshould: '))
    for val in prices:
        if val < val_thr:
            print('there is at least one price under', val_thr)
            return
    print('there are no prices under', val_thr)

def TT_plan(prices):
    possible_list = []
    difference_of_day = 1
    # the initial value can be a positive arbitrary number
    max_difference_of_price = 10
    buy_day = 0
    buy_price = prices[0]
    sell_day = 0
    sell_price = prices[0]
    for index in range(len(prices)):
        for val in prices[(index + 1):]:
            diffence = prices[index] - val
            if diffence < 0:
                if diffence < max_difference_of_price:
                    max_difference_of_price = diffence
                    buy_day = index
                    buy_price = prices[index]
                    sell_day = index + difference_of_day
                    sell_price = val
            difference_of_day += 1
        difference_of_day = 1
    if max_difference_of_price == 10:
        print('All prices are same!')
    else:
        print('Buy on day', buy_day, 'at price', buy_price )
        print('Sell on day', sell_day, 'at price', sell_price)
        print('Total profit:', max_difference_of_price*(-1))

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average_price(prices)
        elif choice == 4:
            standard_deviation(prices)
        elif choice == 5:
            max_price(prices)
        elif choice == 6:
            threshould(prices)
        elif choice == 7:
            TT_plan(prices)
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')

tts()
