#Use Python 2.7
def add(*args):           #args takes multiple inputs in the form of a list, | VARIABLE PARAMETERS |
    s = 0
    for elements in args: #for every number in the list
        s = s + elements  #iterate on every number/element starting from 0 to last element, ie: in this case 5.
    return s              #return the final answer.
print add(1,2,5)          #calling this function will print the final answer that is stored in s. We can input as many parameters we want.