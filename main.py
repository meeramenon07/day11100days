print("Day 11 Challenge \n", "How many seconds are in a year?")
oneMinute = int(input("How many seconds in one minute?: "))
oneHour = int(input("How many minutes in one hour?: "))
oneDay = int(input("How many hours in one day?: "))
oneMonth = int(input("How many months in one year?: "))
days_oneYear = int(input("How many days in one Year?: "))
#days_leapYear = int(input("How many days in a leap Year"))
if days_oneYear == 365:
  result = 365 * 24 * 60 * 60
  print("There are", result, "seconds in a Year")
else:
  result = (365 + 1) * 24 * 60 * 60
  print("There are", result, "seconds in a leap year")
  
  
