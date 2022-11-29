# allows him to enter a value representing the number of minutes
minutes = int(input("please enter the number of (whole) minutes worked this month"))


hours = int (minutes / 60)
minutes = int(minutes % 60)
days = int(hours / 8)
leftoverhours = int(hours % 8) 

print("{0}:{1}:{2}".format(days,hours,minutes))

