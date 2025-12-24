import json
import os
import random

from pyscript import display, when, window, document

import keyboard

russian_keyboard = keyboard.Russian()

def setup():
    word_book = os.path.join(os.path.curdir, "word_book/de_ru/book.json")

    with open(word_book, "r") as f:
        words = json.load(f)["test4"]

    word_key = list(words.keys())
    random.shuffle(word_key)

    print(word_key)

    return words, word_key


class Status:
    def __init__(self):
        self.correct_translation = 0
        self.master_dict, self.master_list = setup()
        self.completed_list: list[str] = self.master_list.copy()
        self.current_russian_word = self.master_dict.get(self.completed_list[0], "ERROR")

    def update_russian_word(self):
        self.current_russian_word = self.master_dict.get(self.completed_list[0], "ERROR")



status = Status()

def update_word(word: str, target="test") -> None:
    display(word, target=target, append=False)

def CLI() -> None:
    print("Infinite loop, escape with: Ctrl + C")
    for i in status.master_list:

        print(f"Was ist die Korrekte Schreibweise von {i}")
        input("Denkst du hast es fertig? (Drücke Enter)")

        if input(f"\nDie Korrekte Version wäre {status.master_dict[i]} hast du es richtig[y/N]").strip().lower() == "y":
            print("GUT GEMACHT")

        else:
            print("SCHADE")

        print("\n")


def website_setup():
    update_word(status.completed_list[0])
    update_word("0", target="finished_so_far")
    update_word(str(len(status.master_list)), target="finished_number")
    status.completed_list.remove(status.completed_list[0])


@when("click", "#next_buttom")
def next_button():
    update_word(str(len(status.master_list) - (len(status.completed_list))), target="finished_so_far")
    update_word("_______", target="reveal")
    update_word("", target="correct")
    document.getElementById("user_input").value = ""

    if not status.completed_list:
        update_word("GLÜCKWUNSCH, DU HAST ALLE WÖRTER DURCH,\nLade die Seite neu um weiter zu machen")
        return
    update_word(status.completed_list[0])
    status.update_russian_word()
    status.completed_list.remove(status.completed_list[0])

@when("click", "#go_to_repo")
def change_url_to_github_repo():
    window.location.href = "https://github.com/Platzhalten/sprache"


@when("click", "#finished_buttom")
def reveal_solution():
    update_word(status.current_russian_word, target="reveal")
    user_input:str = document.getElementById("user_input").value

    user_input = user_input.strip().lower()

    if user_input == status.current_russian_word.lower():
        update_word("Glückwunsch, du hast es richtig übersetzt", target="correct")
        status.correct_translation += 1
    else:
        update_word("Schade du hast es falsch übersetzt", target="correct")

website_setup()
