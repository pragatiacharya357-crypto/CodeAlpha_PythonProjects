import random

words = ["python", "hangman", "developer", "internship", "coding"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:

    # display word state
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
    print("Letters guessed:", guessed_letters)

    guess = input("Guess a letter: ").lower().strip()

    # 🛑 VALIDATION FIX (IMPORTANT)
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter ONLY a single alphabet letter.")
        continue

    # already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        wrong_guesses += 1

    # win condition
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

else:
    print("\n💀 Game Over! The word was:", word)