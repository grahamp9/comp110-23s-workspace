"""Ask user for number, give hints about number if wrong"""

SECRET: int = 10 
guess: int = int(input("Guess a number!"))
playing: bool = True 

while playing:
    if guess == SECRET: 
        print("Correct, you did it!")
        playing = False
    else: 
        if guess == 9:
            print ("SO CLOSE!")
        if guess % 2 == 1:
            print("Your guess is odd. The answer is even. ")
        else:
            if guess < SECRET: 
                print ("Too low! ")
                print ("SO CLOSE!")
            else: #guess is > secret 
                print ("Too high! ")    
        guess = int (input("Wrong guess, try again!"))