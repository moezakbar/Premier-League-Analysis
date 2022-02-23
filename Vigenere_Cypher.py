"""
This is a program that will prompt the user for some text and a keyword, and then display the Vigenère encrypted form of the text on the screen.
The Vigenère Cypher is an improvement on the much older Caesar Cypher, in which each letter of a message (or "plaintext") is replaced
by the letter that is offset from the original letter by a fixed amount.
"""


#Create a list of all the alphabets
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def vigenere_table(alphabets):
    """
    This function creates a dictionary containing alphabets as keys and a list of
    corresponding alphabets as values.

    Parameters - alphabets: A list containing alphabets
    Return - table: A dictionary representing the vigenere table
    """

    #Create an empty dictionary which will hold the data of the vigenere table
    table = {}

    #Create a loop that will iterate 26 times
    for x in range(len(alphabets)):

        #Add all the letters as keys(rows) and the letters including
        #and after that particular letters as values
        table[alphabets[x]] = alphabets[x:]
        #Find out hte length of the list of all the values
        length_of_list = len(table[alphabets[x]])

        #Check to see if the length of the value is not equal to 26
        if length_of_list != 26:

            #Subtract the length of the value from 26 to see how many letters are remaining
            remaining_index = 26 - length_of_list
            #Create a copy of the alphabets list so that there are no changes to the original list
            new_alphabets = alphabets.copy()

            #A loop that will iterate in the range of the remaining index
            for y in range(remaining_index):
                #Add all the remaining letters from the original list to the end of the copied list
                new_alphabets.append(alphabets[y])

            #Add the new alphabets list as the value of that partcular key
            table[alphabets[x]] = new_alphabets[x:]

    #Return the dictionary to the functon that called it
    return table


def remove_non_alphabets(text):
    """
    This function removes all the non-alphabets from the plaintext.

    Parameters - text: A string value
    Return - new_text: A string value that does not contain any non-alphabet character
    """

    #Create an empty string for the new plaintext
    new_text = ''

    #A loop that iterates over each character in the plaintext
    for x in text:

        #Check to see if the character is an alphabet
        if x.isalpha()==True:
            #Add the character to the new string
            new_text+=x

    #Return the string
    return new_text


def line_plaintext_key(text, key):
    """
    This function changes the length of the string of 'key' in such a way
    that it is equal to the length of the string 'plaintext(text)'.

    Parameter - text: A string value
    Parameter - key: A string value
    Return - key: A string
    """

    #Calculate how the difference in lengths of plaintext and key
    length_difference = len(text) - len(key)

    #Check to see if the difference is positive
    if length_difference > 0:

        #A loop that iterates the number of times the length difference is
        for x in range(length_difference):
            #Add the letters of string to the end of the string
            key += key[x]

    #Check to see if the length difference is negative
    elif length_difference < 0:

        #Calculate how many letters of the key need to be removed to match with plaintext
        key_length_difference = len(key) - (length_difference*-1) #convert negative number to positive
        #Remove the extra letters of the key from the end
        key = key[:key_length_difference]

    #Return the key
    return key


def encryption(table,plaintext,key,alphabets):
    """
    This function creates the encrypted form of the plaintext.

    Parameter - table: A dictionary representing the vigenere table
    Parameter - plaintext: A string
    Parameter - key: A string
    Parameter - alphabets: A list of alphabets from a-z
    Return - encrypted_string: A string representing the encrypted form
    """

    #Create an empty string
    encrypted_string = ''
    #Create a local variable which will be used in the for loop
    index_number = 0

    #A loop that iterates the length of the plaintext times
    for x in range(len(plaintext)):

        #A loop that iterates over all the alphabets in the list
        for y in alphabets:

            #Check to see if the character in the plaintext is equal to the alphabet in the list
            if y == plaintext[x]:
                #Find out how far away the alphabet is from letter a
                index_number = alphabets.index(y)

        #Go to the corresponding row in the dictionary according to the character in the key
        #Go to the corresponding value in the list of alphabets according to the index number
        encrypted_string += table[key[x]][index_number]

    #Return the encrypted string
    return encrypted_string


def main():
    """This function controls the flow of the program"""

    #Call the vigenere_table() function to create a table
    table = vigenere_table(alphabets)
    #Ask the user to enter a plaintext
    plaintext = input('Please enter the plaintext: ')
    #Ask the user to enter a key
    key = input('please enter the key: ')
    #Capitalize all alphabets of the plaintext
    plaintext = plaintext.upper()
    #Capitalize all alphabets of the key
    key = key.upper()
    #Call the remove_non_alphabets() function to remove all non-alphabets from plaintext
    plaintext = remove_non_alphabets(plaintext)
    #Call the line_plaintext_key() function to convert key and plaintext into the same length
    key = line_plaintext_key(plaintext, key)
    #Call the encryption() function to form the encrypted message
    encrypted_message = encryption(table,plaintext,key,alphabets)
    #Print the encrypted message
    print('The encrypted message is:', encrypted_message)

#Call the main function
main()
