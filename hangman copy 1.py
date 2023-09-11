#hangman game
def main():

    #to get a random word
    from random_word import RandomWords
    
    print("Welcome to hangman!\n")

    #word types to use throughout function
    r = RandomWords()
    word_str = (r.get_random_word()).lower()
    word = list(word_str)
    empty_word = (list("-"*(len(word))))

    #incase there is a space within the word_str
    for i in range(len(word)):
        if word[i] == " ":
            empty_word[i] = " "

    #creates a --- varient to be more ledgable
    dashes_varient = ""
    for i in empty_word:
        dashes_varient = dashes_varient + i
            
    print("Try to guess the word; this is what your starting with.\n")
    print(dashes_varient)
    print()
    
    print("Also don't guess wrong 10 times or else you lose ... anyway goodluck!\n")

    letter = (input("Time to guess. Please guess a singular letter: ")).lower()

    #baselines for function
    strikes = 0
    total_strikes = 0
    guesses_set = []
    x = -1
    
    hang(x, word, letter, empty_word, strikes, total_strikes, guesses_set, dashes_varient, word_str)
    
def hang(x, word, letter, empty_word, strikes, total_strikes, guesses_set, dashes_varient, word_str):

    #if they guessed that letter already
    while letter in guesses_set:
        letter = (input("You already guessed this! Guess again: ").lower())

    #if they try to guess more than one letter
    while len(letter) >= 2:
        letter = (input("Please only guess one letter! Guess again: ").lower())
        

    #if the guess is not a letter
    while not letter.isalpha():
        letter = (input("This is not a valid letter, guess again: ").lower())
        
    #changing to make sure you stay within range when checking their guess 
    x+= 1

    #if they guessed it 
    if word == empty_word:
        print()
        return print(f"Congrats you guessed right, the word was: {word_str}")

    #checking there guess
    elif x != len(word):
        if word[x] == letter:
            empty_word[x] = letter
            
            #changing the strikes to show they got it
            hang(x, word, letter, empty_word, 1, total_strikes, guesses_set, dashes_varient, word_str)
        else:
            hang(x, word, letter, empty_word, strikes, total_strikes, guesses_set, dashes_varient, word_str)

    else:
        
        #once their guess has been checked add it to a new list so it cant be guessed again
        guesses_set.append(letter)

        #if they got the guess right
        if strikes == 1:
            print("Great guess, you got it!")
            
        #determing num of guesses
        elif strikes == 0:
            total_strikes = total_strikes + 1

            #how many more they have
            guesses_left = 10 - total_strikes
            
            if total_strikes != 10:
                print(f"Wrong!!! You now have {total_strikes} strike, only {guesses_left} guess left!")
            else:

                #if they guessed 10 times
                print()
                print(f"You lose! Better luck next time.")
                print(f"You got this {dashes_varient}")
                return print(f"The right answer is: {word_str}")

        #keeps the --- format
        dashes_varient = ""
        for i in empty_word:
            dashes_varient = dashes_varient + i

        print()
        print(dashes_varient)
        print()

        #showing the player what they have guessed
        the_guesses = guesses_set[0]
        if len(guesses_set) >= 2:
            for i in guesses_set:
                
                #bypass to correctly output the ,'s
                if i == guesses_set[0]:
                    pass
                else:
                    the_guesses = the_guesses + ", " + i

        print(f"Here our your guesses so far: {the_guesses}")

        #guess another letter if they still have guesses
        hang(-1, word,(input("Try again, type another letter: ").lower()), empty_word, 0, total_strikes, guesses_set, dashes_varient, word_str)


main()
