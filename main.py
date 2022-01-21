# Importing random library to choose a random word from a list of words
import random
# Opening a file to read the words in it
file=open('words.txt','r')
# Creating an empty list to store all the words present in the file
words=[]
for word in file:
    word=word.strip().lower()
    words.append(word)

# defining a function to generate a random word with minimum required length
def get_random_word(req_len):
    wordlist=[]
    for word in words:
        if len(word)>=req_len:
            wordlist.append(word)
    return random.choice(wordlist)

# initializing a variable for user to choose the max number of attempts required to guess a word
while True:
    req_attempts = input("Enter the maximum number of attempts you require to guess a word : ")
    # Using try and except method to verify that the input is a number that lies between 1 to 25
    try:
        req_attempts = int(req_attempts)
        if 1 <= req_attempts <= 25:
            print("Maximum Attempts possible are {}".format(req_attempts))
            break
        else:
            print("Please Enter a Number between 1 to 25")
    except:
        print("Please Enter a valid number between 1 to 25")

# initializing a variable for user to choose the min word length required to guess a word
while True:
    req_length = input("Enter the minimum required length of the word you want to guess : ")
    # Using try and except method to verify that the input is a number that lies between 4 to 15
    try:
        req_length = int(req_length)
        if 4 <= req_length <= 15:
            print("Minimum required length of the word is set as {}".format(req_length))
            break
        else:
            print("Please Enter a Number between 4 to 15")
    except:
        print("Please Enter a valid number between 4 to 15")

# Assigning randomly generated word to a variables to store and display the player's guesses
given_word=get_random_word(req_length)
display_word=given_word

# Randomly generating two indexes to display them for the user to guess the word
x=random.randint(0,len(given_word)-1)
y=random.randint(0,len(given_word)-1)

# Replacing each letter in the word with '_' for displaying
for i in range(len(display_word)):
    if i != x and i != y:
        display_word=display_word[0:i]+"_"+display_word[i+1:]

print("Guess the following word : ", " ".join(display_word),"\n")

#Creating a empty list to store all the letters guessed by the user
guessed_letters=[]
attempts=0
while display_word!=given_word:
    # condition to check the number of attempts made by user and to restrict him from making attempts more than given.
    if attempts<req_attempts:
        # initializing a variable for user to guess a letter
        while True:
            guess = input("Enter a letter : ")
            # Using try and except method to verify that the input is a single alphabet.
            try:
                if len(guess) == 1 and guess.isalpha() == True:
                    break
                else:
                    print("Please Enter a single letter")
            except:
                print("Please Enter a letter")
        guess = guess.lower()
        guessed_letters.append(guess)
        attempts += 1
        for i in range(len(given_word)):
            if given_word[i] == guess:
                display_word = display_word[0:i] + guess + display_word[i + 1:]
        print(" ".join(display_word))
        print("Letters guessed : ", guessed_letters)
        print("Attempts Made : ", attempts,"\n")

    else:
        print("Sorry, you reached maximum number of possible attempts")
        print("Better luck Next time!")
        break

#Print the string with guessed letters
if display_word==given_word:
    print("Yayy!! you guessed it right, It's {}".format(given_word.upper()))
