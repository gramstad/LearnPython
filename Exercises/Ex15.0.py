# Imports the argv module
from sys import argv
# Designates argv as the variable 'filename'
script, filename = argv
# Defines the txt file to be read as the variable filename combined with the open command
txt = open(filename)
# Prints the name of the file using the filename variable
print "Here's your file %r:" % filename
# Prints the contents of a txt file
print txt.read()
# Requests the filename be typed in again as raw_input
print "Type the filename again:"
# Sets up a prompt with > character to accept a new filename variable
file_again = raw_input("> ")
# defines a variable as the open command/ filename
txt_again = open(file_again)
# Will print the filename entered
print txt_again.read()