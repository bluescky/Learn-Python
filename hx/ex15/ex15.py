from sys import argv

script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again, 'w+')

temp = "1234567"

txt_again.write(temp)
txt_again.seek(0)
print txt_again.read()

txt_again.close()