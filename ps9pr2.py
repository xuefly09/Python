#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A class to represent calendar dates   
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####
    # 1
    def tomorrow(self):
        if self.month == 12:
            if self.day == 31:
                self.year += 1
                self.month = 1
                self.day = 1
            else:
                self.day += 1
        elif self.month == 2 and self.day > 27:
            if self.is_leap_year() == False:
                self.month = 3
                self.day = 1
            else:
                if self.day == 29:
                    self.month = 3
                    self.day = 1
                else:
                    self.day += 1
        else:
            if self.month <= 7:
                if self.month % 2 == 1 and self.day == 31:
                    self.month += 1
                    self.day = 1
                elif self.month % 2 == 0 and self.day == 30:
                    self.month += 1
                    self.day = 1
                else:
                    self.day += 1
            else:
                if self.month % 2 == 1 and self.day == 30:
                    self.month += 1
                    self.day = 1
                elif self.month % 2 == 0 and self.day == 31:
                    self.month += 1
                    self.day = 1
                else:
                    self.day += 1


    # 2
    def add_n_days(self, n):
        print(self)
        for index in range(n):
            self.tomorrow()
            print(self)

    # 3
    def __eq__(self, other):
        s_s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        s_o = s = '%02d/%02d/%04d' % (other.month, other.day, other.year)
        if s_s == s_o:
            return True
        else:
            return False

    # 4
    def is_before(self, other):
        y_distance = other.year - self.year
        m_distance = other.month - self.month
        d_distance = other.day - self.day
        if y_distance > 0:
            return True
        elif y_distance < 0:
            return False
        elif m_distance > 0:
            return True
        elif m_distance < 0:
            return False
        elif d_distance > 0:
            return True
        elif d_distance < 0:
            return False
        else:
            return False

    # 5
    def is_after(self, other):
        if self == other:
            return False
        if self.is_before(other):
            return False
        else:
            return True

    # 6
    def diff(self, other):
        c_self = self.copy()
        c_other = other.copy()
        res_dat = 0
        increment_v = 0
        if self.is_before(other):
            c_early = c_self
            increment_v = -1
        else:
            c_early = c_other
            increment_v = 1
        while c_self != c_other:
            c_early.tomorrow()
            res_dat += increment_v
        return res_dat

    # 7
    def day_of_week(self):
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        d = Date(4, 8, 2017)
        c_d = self.diff(d)
        return day_of_week_names[-2 + abs(c_d%7)]
