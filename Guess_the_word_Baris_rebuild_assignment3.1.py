import random

#making sure the variabeles exist
game = True
listOfWords = ["apple", "tree", "dragon", "desk", "virtue", "cherry", "poster", "island", "vicious", "horse", "computer", "innuendo", "egg", "cramp", "chocolate", "magician"]
lengthWordToGuess = 0
amountWrong = 0
currentLettersGuessed = []
currentLettersRight = 0
guessesLeft = 10
counter = 0
rightLetters = 0

#making sure that the game keeps running
while game == True:
#main menu screen
    print("Welcome to guess the word!")
    print("1. Start normal game")
    print("2. Start guess mode")
    print("3. Quit Game")
    #this is the moment where the player makes a choice
    choice  = int(input("Please make a choice"))
    #reaction to each choice
    if choice == 1: #mode stable
        #the game put in a defination so that there is more control about which game mode gets activated
        def start_normal_mode():
            #a random word gets chosen from the list that the player needs to guess.
            randomWord = random.choice(listOfWords)
            #hiding every letter of whatever random word is chosen and replace it with a *
            for x in randomWord:
                print("*", end=" ")
            #a reaction for every mistake the player makes
            def hangmanVisualPrint(amountOfWrongs):
                if(amountOfWrongs == 0):
                    print("\n")
                    print("No mistakes were made")
                elif(amountOfWrongs == 1):
                    print("\n")
                    print("Your first mistake.")
                elif(amountOfWrongs == 2):
                    print("\n")
                    print("A second mistake? what are you doing?!")
                elif(amountOfWrongs == 3):
                    print("\n")
                    print("Your third mistake, this is not gonna end well...")
                elif(amountOfWrongs == 4):
                    print("\n")
                    print("Fourth mistake! they will hang you for this!")
                elif(amountOfWrongs == 5):
                    print("\n")
                    print("Fifth mistake, you can't hide any longer.")
                elif(amountOfWrongs == 6):
                    print("\n")
                    print("Your last mistake...")
            #this will be repeated every turn, here the word what has to be guessed gets printed. hiding the letters what hasn't been guessed and uncovering what has been guessed       
            def giveWord(guessedLetters):
                #resetting the values
                counter = 0
                rightLetters = 0
                #this is where letters gets covered/uncovered
                for char in randomWord:
                    #if it has been guessed, then this is where the letters gets uncovered
                    if(char in guessedLetters):
                        print(randomWord[counter], end=" ")
                        rightLetters += 1
                    #if it hasn't been guessed then it will stay hidden
                    else:
                        print("*", end= " ")
                    counter += 1
                return rightLetters
            #setting the values for a new game 
            lengthWordToGuess = len(randomWord)
            amountWrong = 0
            currentLettersGuessed = []
            currentLettersRight = 0
            #checking if current game can still go on + letting the player guess + checking if the guess is wrong or right
            while(amountWrong != 6 and currentLettersRight != lengthWordToGuess):
                #letting the player know what he/she already guessed
                print("\nLetters guessed so far: ")
                for letter in currentLettersGuessed:
                    print(letter, end=" ")
                #this is where the player puts in his/her next guess
                letterGuessed = input("\nGuess a letter")
                #guessed right
                if(letterGuessed in randomWord):
                    hangmanVisualPrint(amountWrong)
                    currentLettersGuessed.append(letterGuessed)
                    currentLettersRight = giveWord(currentLettersGuessed)
                #guessed wrong
                else:
                    amountWrong += 1
                    currentLettersGuessed.append(letterGuessed)
                    hangmanVisualPrint(amountWrong)
                    currentLettersRight = giveWord(currentLettersGuessed)

            #a message to the player when he/she wins/loses
            if(amountWrong == 6):
                print("\nYou made too many mistakes...")
            elif(currentLettersRight == lengthWordToGuess):
                print("\nYou won!")
            #checking if the player wants to continue or not.
            print("\nThe game is over, do you want to play again?")
            userAgain = input("y/n?")
            userAgain = userAgain.lower()
            #reaction based on player answer
            if(userAgain == "y"):
                start_normal_mode()
            elif(userAgain == "n"):
                print("Returning to main menu")
            else:
                print("Not a option, please choose y/n.")
        #start of game after the def got made
        start_normal_mode()
    elif choice == 2:#mode stable
        #the game put in a defination so that there is more control about which game mode gets activated
        def startGuessMode():
            #a random word gets chosen from the list that the player needs to guess.
            randomWord = random.choice(listOfWords)
            #hiding every letter of whatever random word is chosen and replace it with a *
            for x in randomWord:
                print("*", end=" ")
            #a reaction for every mistake the player makes
            def hangmanVisualPrint(guessesLeft):
                if(guessesLeft == 10):
                    print("\n")
                    print("10 guesses left")
                elif(guessesLeft == 9):
                    print("\n")
                    print("9 guesses left")
                elif(guessesLeft == 8):
                    print("\n")
                    print("8 guesses left")
                elif(guessesLeft == 7):
                    print("\n")
                    print("7 guesses left")
                elif(guessesLeft == 6):
                    print("\n")
                    print("6 guesses left")
                elif(guessesLeft == 5):
                    print("\n")
                    print("5 guesses left")
                elif(guessesLeft == 4):
                    print("\n")
                    print("4 guesses left")
                elif(guessesLeft == 3):
                    print("\n")
                    print("3 guesses left")
                    print("Think wisely if you want to make it")
                elif(guessesLeft == 2):
                    print("\n")
                    print("2 guesses left")
                elif(guessesLeft == 1):
                    print("\n")
                    print("1 guesses left")
                elif(guessesLeft == 0):
                    print("\n")
                    print("0 guesses left")
                    print("It was nice knowing you")
            #this will be repeated every turn, here the word what has to be guessed gets printed. hiding the letters what hasn't been guessed and uncovering what has been guessed
            def giveWord(guessedLetters):
                counter = 0
                rightLetters = 0
                for char in randomWord:
                    if(char in guessedLetters):
                        print(randomWord[counter], end=" ")
                        rightLetters += 1
                    else:
                        print("*", end= " ")
                    counter += 1
                return rightLetters
            #setting the values for a new game 
            lengthWordToGuess = len(randomWord)
            guessesLeft = 10
            currentLettersGuessed = []
            currentLettersRight = 0

            #checking if current game can still go on + letting the player guess + checking if the guess is wrong or right
            while(guessesLeft != 0 and currentLettersRight != lengthWordToGuess):
                #letting the player know what he/she already guessed
                print("\nLetters guessed so far: ")
                for letter in currentLettersGuessed:
                    print(letter, end=" ")
                #this is where the player puts in his/her next guess
                letterGuessed = input("\nGuess a letter")
                #if player guesses right
                if(letterGuessed in randomWord):
                    guessesLeft -= 1
                    hangmanVisualPrint(guessesLeft)
                    currentLettersGuessed.append(letterGuessed)
                    currentLettersRight = giveWord(currentLettersGuessed)
                #if player guesses wrong
                else:
                    guessesLeft -= 1
                    currentLettersGuessed.append(letterGuessed)
                    hangmanVisualPrint(guessesLeft)
                    currentLettersRight = giveWord(currentLettersGuessed)
            
            #a message to the player when he/she wins/loses
            if(guessesLeft == 0):
                print("\nYou made too many mistakes...")
            elif(currentLettersRight == lengthWordToGuess):
                print("\nYou won!")
            #checking if the player wants to continue or not.
            print("\nThe game is over, do you want to play again?")
            userAgain = input("y/n?")
            userAgain = userAgain.lower()
            #reaction based on player answer
            if(userAgain == "y"):
                startGuessMode()
            elif(userAgain == "n"):
                print("\nReturning to main menu")
            else:
                print("\nNot a option, please choose y/n.")
        #start of game after the def got made
        startGuessMode()
    #this is the choice made when player wants to quit
    elif choice == 3:
        #the program runs mostly on a while loop. if game = false then the program shuts down. Sending out a goodbye message as confirmation of the shutdown
        game = False
        print("Thank you for playing, have a good day!")
        #if the players puts a invalid option in, the player will be warned about it and has to put in a correct option.
    else:
        print('Invalid option. Please enter a number between 1 and 4.')