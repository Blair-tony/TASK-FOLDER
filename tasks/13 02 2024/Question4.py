#Write a Python program to extract year, month, date and time using Lambda. 

# Sample Output: 

# 2020-01-15 09:03:32.744178 

# 2020 

# 1 

# 15 

# 09:03:32.744178 

h="2020-01-15 09:03:32.744178"

hyear = lambda x: x[0:4]
hmonth = lambda x: x[5:7]
hdate = lambda x: x[8:10]
htime = lambda x: x[11:]


year = hyear(h)
month = hmonth(h)
date = hdate(h)
time = htime(h)


print(year)
print(month)
print(date)
print(time)