"""
In this assignment we use a basic measure of similarity to define a relationship on a set of books. 
For each book in the set, we determine which of the other books is most similar to it.
The similarity measure that we will use is the jaccard similarity.
The chosen books have been bundled together for your convenience into the file Books_used_for_assignment2.zip
You will need to download and unzip this file. The file is uploaded in the repository.
A file containing stopwords_used_for_assignment2 is also uploaded in the repository. Stopwords are removed from the 
books before the jaccard similarity is applied to them.
"""

#import all the functions that will be used
from tkinter.filedialog import askdirectory
import glob
import tkinter as tk

def remove_non_alpha(word):
    """
    This function removes all the non-alphabetic characters from a string.
    Parameter: word - a string
    Return: new_word - a string
    """

    #create an empty string
    new_word = ''

    #iterate through each character in the string
    for character in word:

        #check to see if the character is alphabetic
        if character.isalpha():

            #add the character to the empty string
            new_word += character

    #return the updated string
    return new_word


def signature(text_files,stopWords):
    """
    This function counts the words in all the books excluding the stop words, and then
    chooses the top 25 words in each book. It adds the top 25 words of each book to a
    dictionary alongside its respective book and returns it.
    Parameters: text_files - a list of all book files
                stopWords - a list of stopWords
    Return: books_signature -  a dictionary containing top 25 words of each book
    """
    #create an empty dictionary
    books_signature = {}

    #iterate the length of text_files times
    for file_number in range(len(text_files)):

        #create an empty dictionary to count words
        word_counter = {}
        #create an empty list for the top 25 words
        top_25_words = []
        #open and read through each file
        file = open(text_files[file_number],'r',encoding='utf-8')

        #iterate through each line in the file
        for line in file:

            #add each word in the line to a list
            line_list = line.split()

            #iterate through each word in the list
            for word in line_list:

                #call the function that removes non-alphabetic letters
                word = remove_non_alpha(word)
                #convert each word to lower case letters
                word = word.lower()

                #check to see if the word is not a stop word and it is not an empty string
                if word not in stopWords and (len(word)>0):

                    #check to see if the word is already in the dictionary
                    if word in word_counter:

                        #add 1 to the value for that word
                        word_counter[word] += 1

                    #if the word is not in the dictionary
                    else:
                        #add the word to the dictionary with 1 as its value
                        word_counter[word] = 1

        #create an empty string for the frequencies of all the words
        word_frequency = []

        ## add each key : value pair from the dictionary to the list, as a tuple
        for w,f in iter(word_counter.items()):

            word_frequency.append((w,f))

        #sort the list in a descending order and use lambda function to compare the elements
        word_frequency.sort(key = lambda x:x[1], reverse=True)

        #a loop that iterates 25 times
        for z in range(25):

            #add the first element of the tuple to the list
            top_25_words.append(word_frequency[z][0])

        #add the file name and its top 25 words to the dictionary
        books_signature[text_files[file_number]] = top_25_words

    #return the dictionary
    return books_signature


def comparison(book_signature):
    """
    This function converts the values into sets and compares each book's set with
    other sets applying the jaccard similarity formula to determine what book is
    most similar to it. The data is added to a dictionary
    Parameter: book_signature - a dictionary
    Return: similar_books -  a dictionary consisting of books and their most similar book
    """

    #create a dictionary
    similar_books = {}

    #a loop that iterates over each key in a dictionary
    for x in book_signature:

        #convert the values into sets
        book_signature[x] = set(book_signature[x])


    #a loop that iterates over each key in a dictionary
    for key in book_signature.keys():

        #set a variable equal to 0
        maximum = 0

        #a loop that iterates over each key in the dictionary
        for k in book_signature.keys():

            #check to see if the value at the particular iteration of both loops is not same
            if book_signature[k] != book_signature[key]:

                #calculate the intersection of two sets
                intersection = book_signature[key].intersection(book_signature[k])
                #calculate the union of two sets
                union = book_signature[key].union(book_signature[k])
                #calculate the jaccard similarity
                jaccard_similarity = len(intersection) / len(union)

                #check to see if the jaccard similarity of that set is greater than the maximum variable
                if jaccard_similarity > maximum:

                    #set the maximum variable equal to the value of jaccard similarity
                    maximum = jaccard_similarity

                    #find out the file name of the set which has maximum value
                    index_number = k

        #add the file name to a dictionary
        similar_books[key] =  index_number

    #return the dictionary
    return similar_books

def displayOutput(similar_books):
    """
    This function displays the output in a tabular form using tkinter's
    grid layout
    Parameter: similar_books -  a dictionary
    Return: None
    """
    #open the tkinter video
    window = tk.Tk()
    #set the geometry of the tkinter window
    window.geometry("1200x800")
    #create the first column for book name
    col_0_head = tk.Label(window, text=" Book Name ", pady=20)
    #set its grid to first row and first column
    col_0_head.grid(row=0, column=0)
    #make the second column for similar book
    col_1_head = tk.Label(window, text=" Similar Book ")
    #set its grid to first row and second column
    col_1_head.grid(row=0, column=1)

    #set a variable equal to 1
    rows = 1

    #a loop that keeps repeating until it creates 25 rows
    while rows <= 25:

        #a loop that iterates over each key in the dictionary
        for key in similar_books.keys():

            y = tk.Label(window, text = key)
            #write down the text under column one with rows changing after each iteration
            y.grid(row = rows, column = 0)
            #add one to the row to move onto the next row
            rows += 1

    #set the variable back to 1
    rows = 1

    #a loop that keeps repeating until 25 rows are created
    while rows <= 25:

        #a loop that iterates over each key in the dictionary
        for key in similar_books.keys():

            z = tk.Label(window, text = similar_books[key])
            #write down the text under column one with the rows changing after each iteration
            z.grid(row = rows, column = 1)
            #add 1 to the row to move onto the next row
            rows += 1

    #keep it in a loop
    window.mainloop()


def main():
    #create an empty list for stop words
    stopWords = []
    #open and read the stopwords file
    stop_words = open('Stopwords.txt', 'r')


    #a loop that reads over each line of the stopwords file
    for x in stop_words:

        #remove the '\n' from the end of each word
        new_word = x.rstrip('\n')
        #add the word to the stopwords list
        stopWords.append(new_word)

    data_directory = askdirectory(initialdir=r"C:\Users\Jeff\Books")
    #create a list of all the file names
    text_files = glob.glob(data_directory + "/" + "*.txt")
    #call the function that creates the signature for each book
    book_signature = signature(text_files,stopWords)
    #call the function that finds the similarity between each book
    similar_books = comparison(book_signature)
    #call the fucntion that displays the output on tkinter
    displayOutput(similar_books)

#call the main function
main()
