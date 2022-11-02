import random
import word_list
import ascii_art

game_on = True

# I use a while loop here to add replayability
while True:
    # define the variables for the game
    stages = ascii_art.stages
    chosen_word = random.choice(word_list.word_list)
    word_length = len(chosen_word)
    display = []
    life = 6
    letters = []
    
    # This creates the blank spaces for the game
    for letter in chosen_word:
        display.append("_")

    print(ascii_art.logo)
    print(stages[life])
    print(f"{' '.join(display)}")

    while game_on:

        # Ask the user to guess a letter and assign their answer to a variable called guess.
        guess = input("Guess a letter: ").lower()
        print("\n" * 80)

        # If the letter is wrong you will
        if guess not in chosen_word:
            if guess in letters:
                print(f"You have already guessed {guess}, try again!")
            elif guess not in chosen_word:
                life = life - 1
                letters.append(guess)
                print(f"You chose {guess}, this letter is not in the word!\nYou lose a life!")

        # If the letter is correct
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(f"You chose {guess}, this letter is in the word!\nGood job keep going!")

        print(stages[life])
        print(f"{' '.join(display)}")
        print(f"{' '.join(letters)}")
        
        # Win condition
        if not "_" in display:
            print("YOU WIN!")
            game_on = False
        
        # Lose condition
        if life == 0:
            print(f'GAME OVER!\nThe word was "{chosen_word}"')
            game_on = False
    
    # replay?
    replay = input("Would you like to play again: Y or N?").lower()
    if replay == "y":
        print("\n" * 80)
        game_on = True
        continue
    else:
        print("Thanks for playing!")
        break
