'''
Name: Matthew Harris
Date: 10/20/24
Description: Unit 2 Homework 1
'''
print('Problem 1'.center(20,'-'))
print(f"Space,\nSwamp,\nand Castle")
print('Problem 2'.center(20,'-'))
print(""" _   |~  _
[_]--'--[_]
|'|""`""|'|
| | /^\ | |
|_|_|I|_|_|""")
print('Problem 3'.center(20,'-'))
distance_to_seattle = 173.8  
miles_per_gallon = int(input("How many miles per gallon does your car get? "))
gas_price = float(input("How much does a gallon of gas cost near your house? "))
tank_capacity = int(input("How many gallons of gas does your car's tank hold? "))
gallons_needed = distance_to_seattle / miles_per_gallon
cost_to_drive = gallons_needed * gas_price
print(f"The cost to drive from Portland to Seattle is approximately ${cost_to_drive:.2f}.")
