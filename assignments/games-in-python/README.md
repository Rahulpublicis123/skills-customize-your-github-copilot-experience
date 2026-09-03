# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game that uses Python strings, loops, conditionals, user input, and random selection. Practice managing game state while giving the player clear feedback about their progress.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Create the starting state for a Hangman game. Select a secret word from a predefined list and prepare the values needed to track the player's progress and remaining attempts.

#### Requirements

Completed program should:

- Store at least five possible words in a predefined list.
- Randomly select one word from the list for each game.
- Track the letters guessed by the player.
- Set and display a maximum number of incorrect guesses allowed.

### 🛠️ Implement the Guessing Loop

#### Description

Write the main game loop so the player can guess letters, reveal matching letters, and receive a final result when the word is guessed or attempts run out.

#### Requirements

Completed program should:

- Accept one-letter guesses from the player and display the current progress using underscores for unguessed letters.
- Decrease the remaining attempts after an incorrect guess and avoid counting a repeated guess twice.
- End when the player reveals every letter or uses all allowed incorrect guesses.
- Display a clear win message or lose message, including the secret word when the player loses.
