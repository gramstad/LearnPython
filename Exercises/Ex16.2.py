from sys import argv

script, filename = argv

print "I'm going to open %s" % filename

myfile = open(filename)

print "Now to read it!"

myfile.read()

print "Now to close the file!"

myfile.close()