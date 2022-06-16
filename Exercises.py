# Exercises

import sys

# Question 1
def turn_clockwise(pos):
    """Returns the next position after pos in a clockwise manner."""
    
    if pos == "N":
        return "E"
    
    elif pos == "E":
        return "S"
    
    elif pos == "S":
        return "W"
    
    elif pos == "W":
        return "N"
    
    return None


# Question 2
def day_name(num):
    """Returns the day of that specific number"""
    
    if num == 0:
        return "Sunday"
    
    elif num == 1:
        return "Monday"
    
    elif num == 2:
        return "Tuesday"
    
    elif num == 3:
        return "Wednesday"
    
    elif num == 4:
        return "Thursday"
    
    elif num == 5:
        return "Friday"
    
    elif num == 6:
        return "Saturday"
    
    return None


# Question 3
def day_num(name):
    """Returns the number of the specific day"""
    
    if name == "Sunday":
        return 0
    
    elif name == "Monday":
        return 1
    
    elif name == "Tuesday":
        return 2
    
    elif name == "Wednesday":
        return 3
    
    elif name == "Thursday":
        return 4
    
    elif name == "Friday":
        return 5
    
    elif name == "Saturday":
        return 6
    
    return None


# Question 4
def day_add(name, delta):
    """Returns the day name after a given delta."""
    
    num = day_num(name)
    final_day_num = (num + delta) % 7
    
    return day_name(final_day_num)


# Question 5
def days_in_month(month_name):
    """Returns the number of days of the given month."""
    
    if month_name == "January":
        return 31
    
    elif month_name == "February":
        return 28
    
    elif month_name == "March":
        return 31
    
    elif month_name == "April":
        return 30
    
    elif month_name == "May":
        return 31
    
    elif month_name == "June":
        return 30
    
    elif month_name == "July":
        return 31
    
    elif month_name == "August":
        return 31
    
    elif month_name == "September":
        return 30
    
    elif month_name == "October":
        return 31
    
    elif month_name == "November":
        return 30
    
    elif month_name == "December":
        return 31
    
    return None


# Question 7 and Question 8
def to_secs(hrs, mins, secs):
    """Returns the total number of seconds with the help of the given hours, minutes and seconds."""
    
    hrs_to_mins = hrs * 60
    total_mins = hrs_to_mins + mins
    mins_to_secs = total_mins * 60
    total_secs = mins_to_secs + secs
    
    return int(total_secs)


# Question 9
def hours_in(secs):
    """Returns the number of hours in the given number of seconds."""
    
    return secs // 3600


def minutes_in(secs):
    """Returns the number of minutes in the given number of seconds."""
    
    return ((secs - (secs % 60)) // 60) - (secs // 3600) * 60


def seconds_in(secs):
    """Returns the number of valid seconds in the given number of seconds."""
    
    return secs % 60


# Question 11
def compare(a, b):
    """Returns 1 if a > b, 0 if a == b, and -1 if a < b."""
    
    if a > b:
        return 1
    
    elif a == b:
        return 0
    
    return -1


# Question 12
def hypotenuse(leg1, leg2):
    """Returns the length of the hypotenuse of a right angle triangle with it's legs"""
    
    return (leg1**2 + leg2**2) ** 0.5


# Question 13
def slope(x1, y1, x2, y2):
    """Returns the distance between (x1, y1) and (x2, y2) points."""
    
    dist_x = x2 - x1
    dist_y = y2 - y1
    
    return dist_y / dist_x


def intercept(x1, y1, x2, y2):
    """Returns the y-intercept of a line with two points: (x1, y1) and (x2, y2)."""
    
    m = slope(x1, y1, x2, y2)
    
    return y1 - m * x1


# Question 14
def is_even(n):
    """Returns True is n is an even number and False if it is an odd number."""
    
    return n % 2 == 0


# Question 15
def is_odd(n):
    """Returns True is n is an odd number and False if it is an even number."""
    
    return n % 2 == 1


# Modified is_odd()
def is_odd(n):
    """Returns True is n is an odd number and False if it is an even number."""
    
    return not is_even(n)


# Question 16
def is_factor(f, n):
    """Returns True if f is a factor of n and False if not."""
    
    return n % f == 0


# Question 17
def is_multiple(m, n):
    """Returns True if m is a multiple of n and False if not."""
    
    return m % n == 0


# Modified is_multiple()
def is_multiple(m, n):
    """Returns True if m is a multiple of n and False if not."""

    return is_factor(n, m)


# Question 18
def f2c(t):
    """Returns the Celsius temperature with the given Fahrenheit temperature."""
    
    return round(5/9 * (t - 32))


# Question 19
def c2f(t):
    """Returns the Fahrenheit temperature with the given Celsius temperature."""
    
    return round(9/5 * t + 32)


# The test functions
def test(did_pass):
    """Checks whether a given test passed"""
    
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "The test at line {0} passed.".format(linenum)
    else:
        msg = "The test at line {0} failed.".format(linenum)
        
    print(msg)
    

def test_suite():
    """Maintains a suite for all the tests."""
    
    # Tests of Question 1
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    
    # Tests of Question 2
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    
    # Tests of Question 3
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    
    # Tests of Question 4
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    
    # Tests of Question 5
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    
    # Tests of Question 6
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("Monday") == None)
    
    # Tests of Question 7
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    
    # Tests of Question 8
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)

    # Tests of Question 9
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

    # Answers of Question 10
    test(3 % 4 == 0)
    test(3 / 4 == 0)
    test(4-2+2 == 0)
    # The above tests will fail
    
    # Tests of Question 11
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    
    # Tests of Question 12
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    
    # Tests of Question 13
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    
    # Tests of Question 14
    test(is_even(2))
    test(is_even(12))
    test(is_even(46))
    test(is_even(52))
    
    # Tests of Question 15
    test(is_odd(1))
    test(is_odd(53))
    # After adding modifications
    test(is_odd(3))
    test(is_odd(5))
    
    # Tests of Question 16
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    
    # Tests of Question 17
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    
    # Tests of Question 18
    test(f2c(212) == 100)
    test(f2c(32) == 0)
    test(f2c(-40) == -40)
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    
    # Tests of Question 19
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


# Printing down the result of all the tests
test_suite()