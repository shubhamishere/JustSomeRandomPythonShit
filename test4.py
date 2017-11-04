#Use Python 63
while 1:
    name = input("Enter your name: ")
    if name != "Joe":
        continue    #what does CONTINUE do: if the name is other than Joe jump back to the start of the loop nad reevaluate the loops condition. If name is Joe then only go to the next line ie: line 6.
    password  = input("Hello Joe what is the password? (It is a fish.): ")
    if password == "swordfish":
       print ("Access granted")
       break