"""
This implements a simplified version of Wheel of Fortune. The computer chooses a word
from a list of words and the user guesses letters until they have filled in all the letters 
in the word or have guessed incorrectly 5 times.

Date:  Oct'28, 2021
"""

#import random function which will be used later
import random

def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the word
    """
    #create a list of words to choose from
    validWords = ["generation", "consume", "computing", "residence", "memory", "hosting"]
    #choose a random word from the list and return it
    return validWords[random.randint(0,5)]

def printStringWithSpaces(word):
    """
    This function prints the word representation (eg: "__r_")
    on the screen with spaces between each underscore/letter
    so that the user can better see how many letters there are.
    Parameter: string
    Return Value:  None
    """
    #create a for loop that iterates through each character of the word
    for x in word:
        #print each character with spaces
        print(x, end=' ')
    #leave two lines for cleaner output    
    print()
    print()

def convertToUnderscores(word):
    """
    Creates a string consisting of len(word) underscores.
    For example, if word = "cat", function returns "___" (3 underscores)

    Parameter: string
    Return Value: string
    """
    #create underscores that are the same length of the word
    underscores = str('_'*len(word))
    #return the underscores
    return underscores
        
def updateWord(currentRep, word, letter):
    """
    This function replaces the underscores with the guessed letter.
    Eg.  letter = 'p', word = "stop", currentRep = "s___" --> returns "s__p"
    Paramters:   currentRep, word are strings
                letter is a string, but a single letter.
    Returns:  a string
    """
    #create an empty string
    newString=""
    #create a for loop that iterates the length of the word times
    for x in range(len(word)):
        #if statement for when the letter is equal the the index position of the word
        if letter==word[x]:
            #add the letter to the empty string
            newString+=letter
        #else statement for when the letter is not equal to the index position of the word 
        else:
            #add the index position of the currentRep at that iteration to the empty string
            newString+=currentRep[x]
    #return newString to the function that called it
    return newString

def updateUsedLetters(usedLetters, letter):
    """
    This function concatenates the guessed letter onto the list of letters
    that have been guessed, returning the result.
    Parameters: string representing the used letters
                string respresenting the current user guess
    Return Value:  string
    """
    #add guessed letter to usedLetters
    usedLetters += letter
    #return the value
    return usedLetters

    
def main():
    """
    This implements the user interface for the program.
    """
    #create an empty list for usedLetters
    usedLetters = ""
    #create a counter for number of wrong guesses
    wrongGuesses = 0

    #call the chooseWord() function and equate it to the variable 'word'
    word = chooseWord()
    #print the output of the function
    print(word)

    #call the convertToUnderscores function and equate it to variable 'currentRep'
    currentRep = convertToUnderscores(word)
    #call the printStringWithSpaces function with currentRep as parameter to display it with spaces
    printStringWithSpaces(currentRep)

    #set checker to true
    continueGame = True

   # create a conditional loop for the checker which checks if it is true
    while continueGame==True:
        #ask the user to guess a letter
        guess = input("Please enter a letter (a-z): ")

        #a conditonal loop that checks if the guessed letter is an alphabet
        while not(guess.isalpha()) or len(guess) != 1:
            #ask the user to enter value again
            guess = input("Please enter valid input(a single letter (a-z)):")

        #convert the user's entered value to lower case
        guess = guess.lower()
        #print the guessed letter
        print("You have guessed ", guess)

        #if statement to check if the guessed letter is not in the already guessed letters
        if not guess in usedLetters:
            #call the updateUsedLetters function to add the letter to usedLetters
            usedLetters=updateUsedLetters(usedLetters,guess)

            #if statement to check if the guessed letter is in the word
            if guess in word:
                #call the updateWord function to replace the underscore with the guessed letter
                currentRep=updateWord(currentRep, word, guess)
                #call the printStringWithSpaces function to display the output with spaces
                printStringWithSpaces(currentRep)

                #if statement to check if currentRep is equal to the word
                if currentRep==word:
                    #print statements to inform the user that they won and game is over
                    print('Congratulations! You have succesfully guessed all the letters.')
                    print('The game is now over. Bye!')
                    #set the checker to false so game stops
                    continueGame=False

            #else statement for if the guessed letter is not found in the word        
            else:
                #add 1 to the counter of wrong guesses
                wrongGuesses+=1
                #print statement to inform the user that the guessed letter was not in the word
                print('The letter is not in the word.')

                #if statement to check if the number of wrong guesses is equal to 5
                if wrongGuesses==5:
                    #inform the user that they have lost
                    print('You have lost the game.')
                    #set the checker to false so game stops
                    continueGame=False

        #else statement for if the guessed letter has already been used before            
        else:
            #inform the user that the letter has already been guessed
            print("You have already guessed that letter!!!")
            print("Here are the letters you have guessed so far: ",end="")
            #call the printWithSpaces function with parameter usedLetters to display the guesses of the user
            printStringWithSpaces(usedLetters)
            
#call the main function
main()
    
    
