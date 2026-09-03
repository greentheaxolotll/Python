import random

WORD_LIST = ["REACT", "HOUSE", "CODEC", "DEBUG", "LOGIC", "ARRAY", "SCOPE", "CLASS", "FUNCS",
    "MERGE", "STACK", "QUEUE", "BUILD", "INPUT", "PRINT", "FALSE", "TRUE", "RANGE", "WHILE",
    "BREAK", "GUESS", "WORDS", "LISTS", "TUPLE", "LAMDA", "FILES", "PORTS", "NODES", "FETCH",
    "STATE", "EVENT", "ROUTE", "QUERY", "PARSE", "HTTPS", "PAGES", "FORMS", "LINKS", "ICONS",
    "MOUSE", "CLICK", "ENTER", "SCORE", "STATS", "LEVEL", "START", "PAUSE", "RESET", "TITLE",
    "ABOUT", "HELPS", "RULES", "PLAYR", "WINER", "LOSER", "ROUND", "TRIES", "LIMIT", "TUTOR",
    "BOOKS", "PENCI", "PAPER", "CHAIR", "TABLE", "LIGHT", "HOUSE", "CARTS", "TRAIN", "PLANE",
    "APPLE", "BANNA", "GRAPE", "MANGO", "PEACH", "PLUMS", "BERRY", "JUICE", "WATER", "COFFE",
    "LEAVE", "MILKS", "SUGAR", "SALTS", "PEEPS", "HERBS", "SPICE", "BAKES", "ROAST", "GRILL",
    "FRYED", "SOUPY", "SALAD", "MEATS", "FISHY", "CHEEK", "MOUTH", "TEETH", "HAIRY", "HAPPY", "LEAFS"]

def get_feedback(guess: str, secret_word: str) -> list[str]:
    #Provides color-coded feedback: Green (!), Yellow (?), Gray (_).
    feedback = ['_'] * 5
    secret_list = list(secret_word)
    guess_list = list(guess)

    for i in range(5):
        if guess_list[i] == secret_list[i]:
            feedback[i] = '!'
            secret_list[i] = None
            guess_list[i] = None


    for i in range(5):
        if guess_list[i] is not None:
            if guess_list[i] in secret_list:
                feedback[i] = '?'
                secret_list[secret_list.index(guess_list[i])] = None

    return feedback

def play_game():
    #Main game loop for Wordle.
    secret_word = random.choice([word for word in WORD_LIST if len(word) == 5])
    attempts = 0
    max_attempts = 6
    print(f"Welcome to Wordle! Guess the 5-letter word in {max_attempts} tries.")

    while attempts < max_attempts:
        guess = input(f"Guess {attempts + 1}: ").strip().upper()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
       

        feedback = get_feedback(guess, secret_word)
        print(f"Feedback: {' '.join(feedback)}")

        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {attempts + 1} attempts!")
            return

        attempts += 1

    print(f"Game over! The secret word was '{secret_word}'.")

if __name__ == "__main__":
    play_game()
