# GHOST BOT
# players take turns choosing letters
# first to complete a word loses
# players can challenge the other if they don't think there is a valid word

scrabble_words_file = open("Collins Scrabble Words (2019).txt", "r")
scrabble_words = scrabble_words_file.read()

# returns whether the ()
def game_loop():
    done = False
    current_string = ""
    print("GAME START!")
    while not done:
        print("Word so far: " + current_string)
        if len(current_string) % 2 == 0:
            player_input = input("Type challenge or a character: ")
            done, current_string = turn(current_string, player_input, False)
        else:
            done, current_string = turn(current_string, bot_input(current_string), True)
        print(10*"-")
    print("Game ended with word: " + current_string)

def turn(current_string, player_input, is_bot):
    if len(player_input) == 1 and player_input.isalpha():
        if valid_word(current_string + player_input):
            print(current_string + player_input + " is a full word! gg!")
            return True, current_string + player_input
        else:
            return False, current_string + player_input
    if player_input == "challenge":
        if is_bot:
            print("You've been challenged!")
            challenge_word = input("Please enter a valid word that starts with \"" + current_string + "\": ")
            if valid_word(challenge_word) and challenge_word[:len(current_string)] == current_string:
                print("Challenger loses!")
                return True, current_string
            else:
                print("Challenger wins!")
                return True, current_string
        else:
            print("You fool") # Have to account for the bot bluffing
            return True, current_string
    else:
        print("Please either type a letter or \"challenge\"")
        return False, current_string

# returns the next character
def bot_input(current_string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not valid_start(current_string):
        return "challenge"
    else:
        score_dict = {}
        for letter in alphabet:
            print(letter)
        
    return "a"

def valid_start(current_string):
    return scrabble_words.find("\n" + current_string.upper()) != -1

# returns true if the word is a valid scrabble word
# (doesn't get aa and zzzs)
def valid_word(word):
    return scrabble_words.find("\n" + word.upper() + "\n") != -1

game_loop()