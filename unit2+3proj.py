'''
Name: Matthew Harris
Date: 4/22/24
Assignment: Unit 2 and 3 Project
'''

month = input("Enter the name of the month: ")
day = int(input("Enter the day: "))
season = "spring"

if (month == "march" and day >= 20) or (month == "april") or (month == "may") or (month == "june" and day < 15):
        season = "Spring"
elif (month == "june" and day >= 15) or (month == "july") or (month == "august") or (month == "september" and day < 22):
        season = "Summer"
elif (month == "september" and day >= 22) or (month == "october") or (month == "november") or (month == "december" and day < 21):
        season = "Fall"
else:
     season = "Winter"
  
print(f"{month} {day} is in {season}")