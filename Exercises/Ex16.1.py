# Imports the argv module 
from sys import argv
# Sets filename as the variable to be unpacked
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# Asks the user for input. RETURN or text input doesn't seem to impact the script but CTRL-C will halt the script.
raw_input("?")
# Prints the message that the file is being opened and calls the open function. The open function uses the filename variable to see which file should be open and the 'w' is a mode, in this case 'w' for 'writing' which is used for truncating the file. Also established the variable target as the name of our text file.
print "Opening the file..."
target = open(filename, 'w')
# Calls the truncate method, which reduces the file's size. Effectively this deletes the text that has been entered in the file.
print "Truncating the file. Goodbye!"
target.truncate()
# Prints the statement asking the user for three lines of input. Each line of input prompts the user with line 1/2/3 and sets each of these as a variable to be used later in the program.
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# Prints the statement that each of these lines will be written to a file. It then writes each line to the txt file to its own line in the file by using the \n command.
print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# Prints the statement that the file is being closed.
print "And finally, we close it."
target.close()