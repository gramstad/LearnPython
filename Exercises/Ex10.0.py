tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Study Drills
#2
print """
Printing in double quotes
"""

print '''
Printing in single quotes
'''

#3   Didn't understand this one. Errors out.
#print \t* "STRINGS!"
#print \t\t\r 'RETURNED STRINGS!'

#4
string_s = "STRINGS"

print "I'm talking %s" % string_s
print "I'm talking %r" % string_s