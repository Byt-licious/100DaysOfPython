#Step 1
word_list = ["adverk", "baboon", "camel"]

#TODO-1-Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random

chosen_word = random.choice(word_list)

#TODO-2- Ask a user to guess a letter and assign their answer to a variable called guess.

guess = input("Guess a letter: ").lower()

#TODO-3- check if the letter the user guessed is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    

end_of_game = False
word_length = len(chosen_word)
while not end_of_game:
    guess = input("Guess aletter").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display [positin] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")       
