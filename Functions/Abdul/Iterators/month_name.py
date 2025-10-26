import calendar as cal 
# print(cal.MONDAY)
# # 0
# print(cal.SUNDAY)
# # 6


# print(cal.day_name[0])  
# # Monday    
# print(cal.day_name[6])
# # Sunday

# list(cal.day_name)
# # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# print(list(cal.day_abbr))
# #['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# # 

# print(list(cal.month_name))
# # ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# print(list(cal.month_abbr))
# # ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


###################

import calendar

def next_month():
    count=1
    while True:
        name=calendar.month_name[count]
        yield name
        count=count%12 +1
        print(count)
        #2 3 4 5 6 7

it=next_month()
print(next(it))  # January
print(next(it))  # February
print(next(it))  # March
print(next(it))  # April
print(next(it))  # May
print(next(it))  # June
print(next(it))  # July

