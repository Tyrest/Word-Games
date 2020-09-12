original_scrabble_words_file = open("Collins Scrabble Words (2019).txt", "r")
optimized_scrabble_file = open("optimized scrabble words.txt", "w")

previous_word = "idk man lmao"

scrabble_words = original_scrabble_words_file.readlines()
for word in scrabble_words:
    if len(previous_word) > len(word) or word[:len(previous_word) - 1] != previous_word[:-1]:
        optimized_scrabble_file.write(word)
        previous_word = word