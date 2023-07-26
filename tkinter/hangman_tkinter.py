from tkinter import *
from PIL import Image, ImageTk
import random

# how to start Tkinter module
root = Tk()
root.title("Hangman")
root.config(bg="white")
root.geometry("1000x1000")


# displays the rules of the game
intro = Label(root, text="Welcome to Hangman!", bg="white", font=200).grid(row=0, column=1)
rules_title = Label(root, text="Rules:", font=75, bg="white").grid(row=1, column=0, sticky="w")
rules1 = Label(root, text="- You have 8 wrong attempts", font=40, bg="white").grid(row=2, column=0, sticky="w")
rules2 = Label(root, text="- You may only guess one letter", font=40, bg="white").grid(row=3, column=0, sticky="w")

# initializes the images, puts them into a list, and displays them
hangman1 = ImageTk.PhotoImage(Image.open("images/hangman_1.jpg"))
hangman2 = ImageTk.PhotoImage(Image.open("images/hangman_2.jpg"))
hangman3 = ImageTk.PhotoImage(Image.open("images/hangman_3.jpg"))
hangman4 = ImageTk.PhotoImage(Image.open("images/hangman_4.jpg"))
hangman5 = ImageTk.PhotoImage(Image.open("images/hangman_5.jpg"))
hangman6 = ImageTk.PhotoImage(Image.open("images/hangman_6.jpg"))
hangman7 = ImageTk.PhotoImage(Image.open("images/hangman_7.jpg"))
hangman8 = ImageTk.PhotoImage(Image.open("images/hangman_8.jpg"))
hangman9 = ImageTk.PhotoImage(Image.open("images/hangman_9.jpg"))
hangman_images = [hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9]
current_image = 0
hangman_display = Label(root, image=hangman_images[current_image])
hangman_display.grid(row=6, column=0)


# initializes the list of possible words and randomly chooses one
with open('text_files/dictionary.txt', 'r', encoding='latin-1') as f:
    dictionary = f.readlines()

dictionary = [word.strip() for word in dictionary]
x = random.randint(0, 84000)
word = dictionary[x]



# initializes a bunch of lists and variables to keep track of all the information
word_list = []
correct_guessed = []
wrong_guessed = []
guessed_list = []
tally = 0
wrong_count = 0
joined_wrong_guessed = ""
second_correct_guessed = []
joined_second_correct_guessed = ""

# counts the letter count and displays it
for letter in word:
    if letter != " ":
        tally += 1
letter_count = Label(root, text=f"HINT: There are {tally} letters in this word", bg="white", font=50).grid(row=5, column=0, sticky="w")

# creates a list to record and display the correctly guessed letters
for letter in word:
    word_list.append(letter)
    if letter != " ":
        correct_guessed.append("_")
    else:
        correct_guessed.append(" ")

# creates a new gcorrect guessed display where the values are seperated by spaces not "_" and displays it
joined_correct_guessed = " ".join(correct_guessed)
display_joined_correct_guessed = Label(root, text=joined_correct_guessed, bg="white", font=75)
display_joined_correct_guessed.grid(row=7, column=0)


# creates a widget where letters can be guessed
user_input = Entry(root, width=35, borderwidth=5)
user_input.grid(row=1, column=1, padx=10, pady=10)


def guess_value():
    """
    This function gets called when someone guesses a letter. It checks if the letter is in the word and then return values based on wether their guess was correct while also changing the image if necessary.
    """

    # initializes all widgets and variables required to store the information and output it
    global wrong_count, joined_wrong_guessed, current_image, guessed_list, second_correct_guessed, joined_second_correct_guessed, word, word_list, guess_button
    value = user_input.get()
    indicator = True
    indicator_count = 0
    indicator_display = Label(root, text="", bg="white", font=40)
    indicator_display.grid(row=2, column=1)
    wrong_count_display = Label(root, text="", bg="white", font=40)
    wrong_count_display.grid(row=4, column=1)
    display_wrong_guessed = Label(root, text="", bg="white", font=40)
    display_wrong_guessed.grid(row=5, column=1)
    display_correct_guessed = Label(root, text="", bg="white", font=40)
    display_correct_guessed.grid(row=5, column=2)

    # checks to make sure the guess is actually a letter
    if value.isalpha() != True:
        error_message_1 = Label(root, text="Error: You can only guess letters", bg="white", font=40)
        error_message_1.grid(row=1, column=2)
        indicator = False
    

    # checks to see if the letter has already been guessed
    for i in guessed_list:
        if i == value:
            error_message_2 = Label(root, text="Error: You can't guess the same letter twice", bg="white", font=40)
            error_message_2.grid(row=1, column=2)
            indicator = False
    

    # checks to see if the guess is only one letter or the actual word
    if len(value) != 1 or len(value) != 1 and value != word:
        error_message_3 = Label(root, text="Error: Can only guess singular letters or correct word", bg="white", font=40)
        error_message_3.grid(row=1, column=2)

    
    # this loop checks to see if the guessed value is in the word and amends the correct guessed list
    if indicator == True:
        for i in range(len(word_list)):
            if value == word_list[i]:
                correct_guessed[i] = value
                indicator_count += 1
                joined_correct_guessed = " ".join(correct_guessed)    

        # this simply checks if the letter was in the word and how many times and of not then it updates the incorrect guessed list
        if indicator_count == 1:
            indicator_display.config(text=(f"{value} is in the word 1 time"))
            display_joined_correct_guessed.config(text=joined_correct_guessed)
            second_correct_guessed.append(value)
            joined_second_correct_guessed = " ".join(second_correct_guessed)
            display_correct_guessed.config(text=f"Correct Guessed: {joined_second_correct_guessed}")
        elif indicator_count > 1:
            indicator_display.config(text=(f"{value} is in the word {indicator_count} times"))
            display_joined_correct_guessed.config(text=joined_correct_guessed)
            display_correct_guessed.config(text=f"Correct Guessed: {joined_correct_guessed}")
            second_correct_guessed.append(value)
            joined_second_correct_guessed = " ".join(second_correct_guessed)
            display_correct_guessed.config(text=f"Correct Guessed: {joined_second_correct_guessed}")
        else:
            wrong_count += 1
            indicator_display.config(text=(f"{value} was not in the word"))
            wrong_guessed.append(value)
            joined_wrong_guessed= " ".join(wrong_guessed)
            display_wrong_guessed.config(text=f"Wrong Guessed: {joined_wrong_guessed}")
            wrong_count_display.config(text=f"Wrong Count: {str(wrong_count)}")
            current_image += 1
            hangman_display.config(image=hangman_images[wrong_count])
        guessed_list.append(value)


    # checks to see if you lost the game
    if wrong_count == 8:
        lose_message = Label(root, text=f"You lost the game. The word was {word}", bg="white", font=40)
        lose_message.grid(row=5, column=3)
        guess_button.config(state=DISABLED)

    
    # checks to see if you won the game
    if value == word or word_list == correct_guessed:
        won_message = Label(root, text=f"Congratulatins you won the game!\nThe word was {word}", bg="white", font=40)
        won_message.grid(row=5,column=3)
        guess_button.config(state=DISABLED)
    
    # clears the guessing widget 
    user_input.delete(0, END)

# creates the button to run the function
guess_button = Button(root, text="Guess", command=guess_value, font=40)
guess_button.grid(row=3, column=1)

# runs the whole program
root.mainloop()