# import datetime
# # import pytz  # Only for linux 

# print(datetime.datetime.now())
# print(datetime.datetime.today())
# #2025-06-27 20:57:14.369630
# #2025-06-27 20:57:14.369630

# #now --> UTC
# #today -> UTC

# # ist=pytz.timezone('Asia/kolkata')

# # print(datetime.datetime.now(ist))
# #2025-06-28 02:27:14.392542+05:30


# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#  # 2025-06-27 17:01:58
#  # https://strftime.org/

# print(datetime.datetime.now().year) # 2025
# print(datetime.datetime.now().hour) # 17
# print(datetime.datetime.now().minute) # 6
# print(datetime.datetime.now().second) # 58



# print(datetime.datetime.fromtimestamp(1730000000)) # 2024-10-25 00:00:00
#     #  2024-10-26 23:33:20 -- no of secs

# print(datetime.datetime.max)
#  #9999-12-31 23:59:59.999999


# from datetime import datetime 

# print(datetime.now())  # Current date and time
#      # 2025-06-27 17:31:35.020260

import datetime 
# import pytz 
print(datetime.datetime.now())
print(datetime.datetime.today())

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # Formatted current date and time

# ist=pytz.timezone('Asia/kolkata')
# print(datetime.datetime.now(ist))
print(datetime.datetime.now().year)  # Current year  -- 2025 
print(datetime.datetime.now().hour)  # Current hour  -- 18
print(datetime.datetime.now().minute)  # Current minute -- 0
print(datetime.datetime.now().second)  # Current second -- 41

print(datetime.datetime.fromtimestamp(1730000000))  # Convert timestamp to datetime
print(datetime.datetime.max)  # Maximum representable datetime

from datetime import datetime
print(datetime.now())  # Current date and time using from datetime import datetime


