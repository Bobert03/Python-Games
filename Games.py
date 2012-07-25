import random
import sys
def main():
    answer = raw_input("Do you want to play a game? y/n." "\n")
    if (answer == 'y'):
        game = raw_input("what game do you want to play?" + "\n" + "we have guess the number (g) and rock paper scissors (r) (isn't working)" + "\n")
        if (game == 'g'):
            guess_number()
        elif (game == 'r'):
            rock_paper_scissors()
        elif (game == 'z'):
            print "def not playing z"
        else:
            print "that game doesn't even exist"
    elif (answer == 'n'):
        print "me niether"
        sys.exit()
    else:
        print "what are you saying"
        main()

def guess_number():
    number = random.randint(1, 10)
    guess = input("Guess a number between 1 and 10. You have three chances." + "\n")
    if (guess == number):
        print "YOU GUESSED IT"
        again = raw_input("Do you want to play again? Or something else? or no? (y = again, n = no, s = something else)" + "\n")
        if (again == 'y'):
            guess_number()
        elif (again == 's'):
            main()
        elif (again == 'n'):
            print "Goodbye, thanks for playing!"
            sys.exit()
    else:
        guess = input("second try: guess the correct number between 1 and 10." + "\n")
        if (guess == number):
            print "YOU GUESSED IT"
            again = raw_input("Do you want to play again? Or something else? or no? (y = again, n = no, s = something else)" + "\n")
            if (again == 'y'):
                guess_number()
            elif (again == 's'):
                main()
            elif (again == 'n'):
                print "Goodbye, thanks for playing!"
                sys.exit()

        else:
            guess = input("LAST CHANCE" + "\n")
            if (guess == number):
                print "finally"
                again = raw_input("Do you want to play again? Or something else? or no? (y = again, n = no, s = something else)" + "\n")
                if (again == 'y'):
                    guess_number()
                elif (again == 's'):
                    main()
                elif (again == 'n'):
                    print "Goodbye, thanks for playing!"
                    sys.exit()
                
            else:
                print "-__-"
                again = raw_input("Do you want to play again? Or something else? or no? (y = again, n = no, s = something else)" + "\n")
                if (again == 'y'):
                    guess_number()
                elif (again == 's'):
                    main()
                elif (again == 'n'):
                    print "Goodbye, thanks for playing!"
                    sys.exit()
def rock_paper_scissors():

    computer = random.randint(1, 3)
    if (computer == 1):
        computer = "rock"
        
    elif (computer == 2):
        computer = "paper"
       
    elif (computer == 3):
        computer = "scissors"
        
    user = raw_input("Choose rock, paper, or scissors" + "\n")

    if (computer == user):
    	print "It's a TIE! Try again"
    	rock_paper_scissors()
    elif(computer == 'rock' and user == 'paper' or computer == 'scissors' and user == 'rock' or computer == 'paper' and user == 'scissors'):

        print "You WIN! You chose %s and the computer had %s" % (user, computer)
        sys.exit()

    elif (computer == 'paper' and user == 'rock' or computer == 'rock' and user == 'scissors' or computer == 'scissors' and user == 'paper'):
        print "You LOSE! You chose %s and the computer had %s" % (user, computer)
        sys.exit()

    else:
        rock_paper_scissors()
main()

