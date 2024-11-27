from datetime import datetime
def leapyear(year):
    if(year % 4==0 and year % 100 !=0) or (year % 400==0):
        return True
    return False

day =int(input("Enter the day: "))
month =int(input("Enter the month: "))
year =int(input("Enter the year: "))
date=datetime(year,month,day)
formatted_date=date.strftime("%d-%m-%Y")
print("Formatted date: ",formatted_date)

if leapyear(year):
    print("ITS LEAP YEAR!!!!!")
else:
    print("ITS NOT A LEAP YEAR!!!!!!")
