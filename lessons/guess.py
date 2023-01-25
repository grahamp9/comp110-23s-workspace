secret: int = 3
guess: int =4
if guess == secret: 
    print("Success!)")
    print(str(guess)+" is the right number ")
else: 
    guess = guess + 1 
    if guess == secret:
        print ("success on 2nd try")
    else: print("wrong guess")
    if (guess == secret - 1):
        print("the guess of " + str(guess) + " is only off by one number! ")