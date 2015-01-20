# Defines the car variable as an integer of 100
cars = 100
# Defines the variable as a floating point integer of 4.0
space_in_a_car = 4.0
# Defines drivers as an integer of 30
drivers = 30
# Defines passengers as an integer of 90
passengers = 90
# Defines cars_not_driven variable as the cars variable (100) minus the drivers variable (30)
cars_not_driven = cars - drivers
# Defines cars_driven as equal to the number of drivers variable (30 in this case)
cars_driven = drivers
# Defines carpool_capacity variable as the product of two different variables
carpool_capacity = cars_driven * space_in_a_car
# Defines carpool_capacity variable as the quotient of two different variables
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills
# 1) The error was raised because the variable in line 7 of the code was not defined and was used in defining average_passengers_per_car in line 8 of the code

# 2) A floating point number is a number that has one or more decimal places.

# 3) See comments above variable definitions.