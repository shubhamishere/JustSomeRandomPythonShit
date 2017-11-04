import random

def randomBall(result):
    if result == 1:
        return "Good shot"
    elif result == 2:
        return "Good one"
    elif result == 3:
        return "Nice one"
    elif result == 5:
        return "Not bad"

r = random.randint(1,5)     #picks up any random number 1 to 5

print(randomBall(r))        #print what is returned as a value from the above function