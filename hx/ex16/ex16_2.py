from sys import argv

script, filename = argv

print "Start to read the file."
f = open(filename, 'r')
print "Start to print the file."
print f.read()
print "Now close the file."
f.close()