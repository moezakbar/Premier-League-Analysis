"""
Date: 3rd November'2021
This program is a game of Bingo. It creates a 5x5 card for each player and calls random items from a list. 
If the random item is in the 5x5 card of a player, it replaces it with 'FOUND'. When one of the three
goals specified before the game begin is completed, the game stops and the winner's name is displayed
"""


import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import random


def main():
    """
    This function controls the flow of your program. This is where all the other functions will be called.
    """
    #call the list_of_items function to read the url and convert it into a list of strings
    list_of_strings = list_of_items()
    #set a variable that will be used to test the while loop
    new_game = 'yes'

    #a conditional loop that keeps repeating until the variable is equal to no
    while new_game!='no':
        #display the 3 goals of the game
        print('The three goals of this game are:')
        print('1.Full Card -- all items on the card must be found\n2.Single Line -- all items in a single horizontal or vertical line must be marked as FOUND\n3.Four Corners -- the items in each of the four corners of the card must be marked as FOUND.')
        #ask the user which goal they want to set
        goal = int(input('Which goal for the round do you want to choose? Please choose a number from 1-3: '))
        #ask the users about the number of players playing
        number_of_players = int(input('Please enter the number of players playing: '))

        #a loop that keeps repeating as long as the number of players are out of range
        while number_of_players<1 or number_of_players>3:
            print('There can only be 1-3 players')
            #ask the user to enter a valid value for number of players
            number_of_players = int(input('Please enter a valid value: '))

        #if statement for if the players are 1
        if number_of_players==1:
            #ask the user for the name of the player
            player1 = input('Please enter the name of player 1: ')
            #call the functio to generate a list of random items for the player and set it equal to a variable
            player1_card = generate_card(list_of_strings)
            print('The card of', player1, 'is:')
            #display the list in a 5x5 grid
            display_card(player1_card)

        #if statement for if the number of players are equal to 2
        elif number_of_players==2:
            #ask the user for the name of player 1
            player1 = input('Please enter the name of player 1: ')
            #call the function to generate a list of random items for the player
            player1_card = generate_card(list_of_strings)
            print('The card of', player1, 'is:')
            #display the list in a 5x5 grid
            display_card(player1_card)
            #leave a line 
            print()
            #ask the user to enter the name of second player
            player2 = input('Please enter the name of player 2: ')
            #call the function to generate a list of random items for the player
            player2_card = generate_card(list_of_strings)
            print('The card of', player2, 'is:')
            #display the list in a 5x5 grid
            display_card(player2_card)

        #if statement for if the number of players are 3    
        elif number_of_players==3:
            #ask the user for the name of the first player
            player1 = input('Please enter the name of player 1: ')
            #call the function to generate a list of random items for the player
            player1_card = generate_card(list_of_strings)
            print('The card of', player1, 'is:')
            #display the list in a 5x5 grid
            display_card(player1_card)
            #leave a line
            print()
            #ask the user for the name second player
            player2 = input('Please enter the name of player 2: ')
            #call the function to generate a list of random items for the player
            player2_card = generate_card(list_of_strings)
            print('The card of', player2, 'is:')
            #display the list in a 5x5 grid
            display_card(player2_card)
            #leave a line
            print()
            #ask the user for the name of the third player
            player3 = input('Please enter the name of player 3: ')
            #call the function to generate a list of random items for the player
            player3_card = generate_card(list_of_strings)
            print('The card of', player3, 'is:')
            #display the list in a 5x5 grid
            display_card(player3_card)

        #leave a line        
        print()
        print()
        #create a variable that will be used to test the while loop
        game=0
        #a list of names of players that won
        winner_names=[]
        #a list of items spotted by the caller
        random_item_list=[]

        #a loop that keeps repeating until the player(s) win
        while winner_names==[]:
    
            #ask the user to enter anything to proceed with the game
            input('The caller has spotted an item. Please enter anything to display the item and updated card(s): ')
            #call the function to choose a random item from the list of strings
            random_item = random.choice(list_of_strings)

            #a loop that keeps repeating until the random item chosen has not already been called
            while random_item in random_item_list:
                #call the function to choose a random item from the list of strings
                random_item = random.choice(list_of_strings)

            #add the random chosen item to the list of random items called    
            random_item_list.append(random_item)
            #leave a line
            print()
            #display the random item chosen
            print('The item spotted is',random_item)
            #leave a line
            print()

            #if the number of players are 1
            if number_of_players==1:
                #call the function to check if the random item is found in the card of player
                new_player1_card = checking_card(player1_card, random_item)
                print('The card of',player1,'is:')
                #display the updated card in a 5x5 grid
                display_card(new_player1_card)
                #leave a line
                print()
                #call the function to see if the player has won
                game = bingo(goal, new_player1_card)
                
                #check to see if the function returned 'BINGO'
                if game=='BINGO':
                    #if the player won, add the name to the the list of winner names
                    winner_names.append(player1)

            #if the number of players in the game are 2
            if number_of_players==2:
                #call the function to check if the random item is found in the card of player 1
                new_player1_card = checking_card(player1_card, random_item)
                #call the function to check if the random item is found in the card of player 2
                new_player2_card = checking_card(player2_card, random_item)
                print('The card of',player1,'is:')
                #display the updated card of player 1 in a 5x5 grid
                display_card(new_player1_card)
                #leave a line
                print()
                print('The card of',player2,'is:')
                #display the updated card of player 2 in a 5x5 grid
                display_card(new_player2_card)
                #leave a line
                print()
                #call to function to see if player 1 won
                game = bingo(goal, new_player1_card)

                #check to see if the function returned 'BINGO'
                if game=='BINGO':
                    #if the player won, add the name to the list of winner names
                    winner_names.append(player1)

                #call the function to see if player 2 has won
                game = bingo(goal, new_player2_card)

                #check to see if the function returned 'BINGO'
                if game=='BINGO':
                    #if the player won, add the name to the list of winner names
                    winner_names.append(player2)


            #if the number of players in the game are 3
            if number_of_players==3:
                #call the function to check if the random item is found in the card of player 1
                new_player1_card = checking_card(player1_card, random_item)
                #call the function to check if the random item is found in the card of player 2
                new_player2_card = checking_card(player2_card, random_item)
                #call the function to check if the random item is found in the card of player 3
                new_player3_card = checking_card(player3_card, random_item)
                print('The card of',player1,'is:')
                #display the updated card of player 1 in a 5x5 grid
                display_card(new_player1_card)

                #leave a line
                print()
                print('The card of',player2,'is:')
                #display the updated card of player 2 in a 5x5 grid
                display_card(new_player2_card)

                #leave a line
                print()
                print('The card of',player3,'is:')
                #display the updated card of player 3 in a 5x5 grid
                display_card(new_player3_card)
                #leave a line
                print()
                #call to function to see if player 1 won
                game = bingo(goal, new_player1_card)

                #check to see if the function returned 'BINGO'
                if game=='BINGO':
                    #if the player won, add the name to the list of winner names
                    winner_names.append(player1)

                #call the function to see if player 2 won
                game = bingo(goal, new_player2_card)

                #check to see if the function returned 'BINGO'
                if game=='BINGO':
                    #if the player won, add the name to the list of winner names
                    winner_names.append(player2)

                #call to function to see if player 3 won
                game = bingo(goal, new_player3_card)

                #check to see if the function returned 'BINGO'
                if game=='BINGO':
                    #if the player won, add the name to the list of winner names
                    winner_names.append(player3)
      
        print('The winner(s) is/are:')
    
        #a loop that iterates over the list of names of players that won
        for m in winner_names:
            #print each name in a new line
            print(m)
        
        #ask the user if they want to play again    
        new_game = input("Do you want to play again? Enter 'yes' if you do. If you do not want to play again, enter 'no': ")
        #if the user wants to play again
        if new_game=='yes':
            #set the list to empty again
            winner_names=[]
            #set the variable equal to 0 again
            game=0

def list_of_items():
    """
    This function reads a url and adds all the items in the url into a list. The list will contain all
    the items that will be used to generate the player's card and call random items.
    Parameters: None
    Return: item_list - A list of strings containing all items
    """
    
    #create an empty list
    item_list=[]
    #open the url
    file = urllib.request.urlopen("https://www.cs.queensu.ca/home/cords2/bingo.txt")

    #a loop that iterates through each line in the url
    for line in file:
        #decode the line
        updated_line=line[:-1].decode('utf-8')
        #add the line to the empty list
        item_list.append(updated_line)

    #return the list
    return item_list


def generate_card(list_of_strings):
    """
    This function generates a card of items for a player. 25 random strings are selected from a list
    and added to the player's card.
    Parameters: list_of_strings - a list of strings
    Return: items - a list of 25 strings
    """
    
    #set an accumulator
    counter=0
    #create an empty list
    items=[]

    #a loop that keeps going until the accumulator is equal to 25
    while counter!=25:
        #choose a random number between 0 and 24
        number = random.randint(0,len(list_of_strings)-1)

        #check to see if the random number is not already in the list of items
        if list_of_strings[number] not in items:
            #add the random number to the list of items
            items.append(list_of_strings[number])
            #add 1 to the accumulator
            counter+=1

    #return the list of random items generated
    return items

def display_card(card):
    """
    This function displays the player card in a 5x5 grid format.
    Parameters: card - a list of 25 strings
    Return: None
    """
    
    #a loop that iterates 24 times
    for x in range(25):
        #print the the element of the card at that particular iteration and format it
        print(card[x], end="\t")
        #move to a new line at the end of every 5th iteration
        if x==4 or x==9 or x==14 or x==19:
            print()
            
    

def checking_card(player, random_item):
    """
    This function goes through the the player's card to check if the randomly called item is
    in the player's card. If it is in the card, that item in the card is replaced with'FOUND'.
    Parameters: player - a list of 25 strings
                random_item - a string
    Return: player - a list of 25 strings
    """
    #a loop that iterates the length of the player card times
    for x in range(len(player)):
        #check to see if the random item called is in the player's card
        if random_item==player[x]:
            #replace the element at that particular iteration with 'FOUND'
            player[x]='FOUND'
            
    #return the updated player's card
    return player


def bingo(goal, player_card):
    """
    This function checks the player's card to see if they have completed one of the three goals that
    they set before the start of each game. If they have completed the set goal, they return a value
    that stops the game.
    Parameters: goal - An integer vale representing the goal the user has selected
                player_card - a list of 25 strings
    Return: 'BINGO' - a string value that will stop the game
    """
    
    #if the user chooses the first goal
    if goal==1:
        #set an accumulator
        counter=0

        #a loop that iterates through each element in the player card
        for x in player_card:
            #check to see if the element at that particular iteration is 'FOUND'
            if x=='FOUND':
                #add 1 to the accumulator
                counter+=1

        #check to see if the accumulator is equal to 25
        if counter==25:
            return 'BINGO'
        else:
            return 0
        
    #check to see if the user chooses the second goal
    if goal==2:

        #check to see if the first horizontal line of the card is all 'FOUND'
        if player_card[0]=='FOUND' and player_card[1]=='FOUND' and player_card[2]=='FOUND' and player_card[3]=='FOUND' and player_card[4]=='FOUND':
            return 'BINGO'
        #check to see if the second horizontal line of the card is all 'FOUND'
        if player_card[5]=='FOUND' and player_card[6]=='FOUND' and player_card[7]=='FOUND' and player_card[8]=='FOUND' and player_card[9]=='FOUND':
            return 'BINGO'
        #check to see if the thrid horizontal line of the card is all 'FOUND'
        if player_card[10]=='FOUND' and player_card[11]=='FOUND' and player_card[12]=='FOUND' and player_card[13]=='FOUND' and player_card[14]=='FOUND':
            return 'BINGO'
        #check to see if the fourth horizontal line of the card is all 'FOUND'
        if player_card[15]=='FOUND' and player_card[16]=='FOUND' and player_card[17]=='FOUND' and player_card[18]=='FOUND' and player_card[19]=='FOUND':
            return 'BINGO'
        #check to see if the fifth horizontal line of the card is all 'FOUND'
        if player_card[20]=='FOUND' and player_card[21]=='FOUND' and player_card[22]=='FOUND' and player_card[23]=='FOUND' and player_card[24]=='FOUND':
            return 'BINGO'

        #create a random variable that will change in the for loop
        a=0
        #set the accumulator equal to 0 again
        counter=0

        #a loop that keeps on repeating until the random variable is not equal to 5
        while a!=5:

            #check to see if the element in the player_card list is equal to 'FOUND'  
            if player_card[a]=='FOUND':

                #a loop that will iterate through each vertical line of the player card through a step value of 5
                for z in range(a,a+21,5):
                    #check to see if the element at that particular iteration is equal to 'FOUND'
                    if player_card[z]=='FOUND':
                        #add 1 to the counter
                        counter+=1

            #check to see if the accumulator is equal to 5
            if counter==5:
                return 'BINGO'
            else:
                #reset the accumulator to 0 and add one to random variable so for loop moves to next vertical line
                counter=0
                a+=1
    
    #check to see if the user chooses the third goal    
    if goal==3:
        #check to see if each of the corner of the card are 'FOUND'
        if player_card[0]=='FOUND' and player_card[4]=='FOUND' and player_card[20]=='FOUND' and player_card[24]=='FOUND':
            return 'BINGO'
          
#call the main function                  
main()
