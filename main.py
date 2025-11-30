import json
import os
import random

word_book = os.path.join(os.path.curdir, "word_book/de_ru/book.json")

with open(word_book, "r") as f:
    words = json.load(f)["test2"]

words_key = list(words.keys())

random.shuffle(words_key)

print("Infinite loop, escape with: Ctrl + C")
for i in words_key:
    #selected_word = random.choice(list(words.keys()))

    print(f"Was ist die Korrekte Schreibweise von {i}")
    input("Denkst du hast es fertig? (Drücke Enter)")

    if input(f"\nDie Korrekte Version wäre {words[i]} hast du es richtig[y/N]").strip().lower() == "y":
        print("GUT GEMACHT")

    else:
        print("SCHADE")

    print("\n")