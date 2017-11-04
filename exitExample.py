#Use Python 2.7
import sys

while True:
    response = raw_input("Input anything: ")
    if response == 'get out':
        sys.exit()
    print "You typed " + response + "."