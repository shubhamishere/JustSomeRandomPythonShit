def spam(divideBy):

    return 84/divideBy

try:
    print(spam(round(float(raw_input("Enter a number: ")))))
except ZeroDivisionError:
    print ("Cannot divide by zero! You asshole.")