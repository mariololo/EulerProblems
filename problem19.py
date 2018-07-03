"""
You are given the following information, but you may prefer to do some research for yourself.


-1 Jan 1900 was a Monday.


-Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.


-A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.


How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAYS = [31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months_days = dict(zip(MONTHS, DAYS))

def is_leap_year(year):

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_month(month, year):
	if is_leap_year(year) and (month == "February"):
		return 29
	else:
		return DAYS[MONTHS.index(month)]

def next_day(name_day, day , month, year):


	next_year = year
	next_month = month

	if is_leap_year(year) and (month == 1):
		if day + 1 > 29:
			next_month = 2
			next_day = 1
		else:
			next_day = day + 1	

	elif day + 1 > DAYS[month]:
		next_month += 1
		next_day = 1

	else:
		next_day = day + 1
		

	
	if next_month == 12:
		next_month = 0
		next_year = year + 1


	next_name_day = (name_day + 1) % 7

	return [next_name_day, next_day , next_month, next_year]


def count_sundays(start_date = [1, "January", 1901], end_date = [31, "December", 2000]):


	name_day = 0
	day = 1       # Day starts at one, the rest at zero
	month = 0
	year = 1900
	sundays = 0

	while year < 2001:
		

		if (year >= start_date[2]) and (name_day == 6) and (day == 1):
			sundays += 1

		[name_day, day , month, year] = next_day(name_day, day , month, year)
		
		#print([NAMES[name_day], day , MONTHS[month], year], sundays)

	return sundays

if __name__ == "__main__":
	print(count_sundays())



