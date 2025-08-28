from random_word import RandomWords
import ascii_art as art
r = RandomWords()


# Return a single random word
"""Initial values"""
word_to_guess = str(r.get_random_word()).lower()
error_count = 0
win_cond = False
correct_guess_count = 0
previos_letters:set=set()
hidden_word:list = []

"""Game Loop"""
print(f" word_to_guess: {word_to_guess}")
for letter in word_to_guess:
    hidden_word.append("_")
print("Welcome to hangman!")
while correct_guess_count< len(word_to_guess) and error_count<10:
    print(f"Word to guess: {hidden_word}")
    guess=input("Please enter your guess: ")
    if guess in word_to_guess and guess not in previos_letters:
        previos_letters.add(guess)
        print("Congrats! Letter is present")
        for i in range(0,len(word_to_guess)):
            if word_to_guess[i] == guess:
                correct_guess_count+=1
                hidden_word[i]=guess
    else:
        error_count+=1
        print("Oops! An error!")
        print(art.ascii_art[error_count])

"""Game End"""
if error_count == 10:
    print(f"You lost! Game over! The word was: {word_to_guess}")
elif correct_guess_count == len(word_to_guess):
    print("Congratulations! You won!")
    print(f"Guessed word: {hidden_word}")

