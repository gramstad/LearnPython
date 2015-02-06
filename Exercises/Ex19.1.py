# defines the function name and default arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# defines text printed when the function is called using variables and adds an empty row at the bottom of the printed function	
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# prints the below statement
print "We can just give the function numbers directly:"
# calls the function using predefined int arguments that will be used as the variables
cheese_and_crackers(20,30)

# prints the below statement
print "OR, we can use variables from our script:"
# defines new variables
amount_of_cheese = 10
amount_of_crackers = 50
# tells the script to use the variables we just created as arguments in the cheese_and_crackers function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints the below statement
print "We can even do math inside too:"
# tells the function to use the arithmetic below as our argument
cheese_and_crackers(10 + 20, 5 + 6)

# prints the below statement
print "And we can combine the two, variables and math:"
# tells the function to use the arithmetic below as our argument
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)