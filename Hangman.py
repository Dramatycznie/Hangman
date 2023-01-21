import random
import time

play_again = True
print("The Hangman Game")
while play_again:
    difficulty = input("Select difficulty level (easy, medium, hard): ").lower()

    if difficulty == "easy":
        word_list = ["cat", "dog", "sun", "moon", "happy"]
        max_incorrect_guesses = 8
    elif difficulty == "medium":
        word_list = ["python", "programming", "language", "computer", "science"]
        max_incorrect_guesses = 6
    elif difficulty == "hard":
        word_list = ["supercalifragilisticexpialidocious", "antidisestablishmentarianism",
                     "floccinaucinihilipilification"]
        max_incorrect_guesses = 4
    else:
        continue
    word = random.choice(word_list)
    correct_letters = []
    incorrect_guesses = 0
    guessed_letters = []
    word_display = "-" * len(word)
    while len(correct_letters) < len(word) and incorrect_guesses < 6:
        print("Guessed letters: " + " ".join(guessed_letters))
        print("Word: " + word_display)
        print("You have", 6 - incorrect_guesses, "chances left.")
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
        else:
            guessed_letters.append(guess)
            if guess in word.lower():
                positions = [i for i in range(len(word)) if word[i] == guess]
                for i in positions:
                    word_display = word_display[:i] + guess + word_display[i + 1:]
                if len(positions) > 1:
                    print("You guessed right!")
                else:
                    print("You guessed right! The letter {} is in the word!".format(guess))
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
    if play_again.lower() in ["yes", "y"]:
        play_again = True
    elif play_again.lower() in ["no", "n"]:
        play_again = False
    else:
        print("Please enter valid answer!")
        play_again = input("Do you want to play again? (yes/no) ").lower()

print("Thanks for playing!")
time.sleep(2)