import random

play_again = True
print("The Hangman Game")
while play_again:
    words = ["python", "programming", "language", "computer", "science"]
    word = random.choice(words)
    correct_letters = []
    incorrect_guesses = 0

    guessed_letters = []
    word_display = "_" * len(word)
    while len(correct_letters) < len(word) and incorrect_guesses < 6:
        print("Guessed letters: " + " ".join(guessed_letters))
        print("Word: " + word_display)
        print("You have", 6 - incorrect_guesses, "chances left.")
        guess = input("Guess a letter: ")
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
        else:
            guessed_letters.append(guess)
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        word_display = word_display[:i] + guess + word_display[i + 1:]
                        print("You guessed right!")
                if word_display == word:
                    print("You guessed the word!")
                    break
            else:
                incorrect_guesses += 1
                print("You guessed wrong!")
    if incorrect_guesses == 6:
        print("You lose! The word was " + word + ".")
    else:
        print("You win! The word was " + word + ".")

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again in ["yes", "y", "Yes", "YES", "Y"]:
        play_again = True
    elif play_again in ["no", "n", "NO", "No", "N"]:
        play_again = False
    else:
        print("Please enter valid answer!")
        play_again = input("Do you want to play again? (yes/no) ").lower()

print("Thanks for playing!")