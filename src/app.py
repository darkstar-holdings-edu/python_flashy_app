from tkinter import Button, Tk
import pandas as pd
import random

from .config import BACKGROUND_COLOR
from .components import Card

APP_NAME = "Flashy"
LANGUAGE_DATA_PATH = "data"


class App(Tk):
    language: str
    language_pack: pd.DataFrame

    card_front: Card
    card_back: Card
    card_status: bool = True

    def __init__(self, language: str) -> None:
        super().__init__()

        self.language = language
        self.load_language_pack()

        self.load_user_interface()

    def load_user_interface(self):
        self.geometry("900x650")
        self.title(APP_NAME)
        self.config(padx=50, pady=50, background=BACKGROUND_COLOR)

        self.card_front = Card(
            image="assets/card_front.png",
            text="English",
            color="black",
        )
        self.card_back = Card(
            image="assets/card_back.png",
            text="Deutsch",
            color="white",
        )

        button = Button(text="Click", command=self.click_handler)
        button.place(x=200, y=550)

        self.next_question()

    def load_language_pack(self):
        try:
            df = pd.read_csv("/".join([LANGUAGE_DATA_PATH, f"{self.language}.csv"]))
        except FileNotFoundError:
            print(f"Invalid language pack: {self.language}")
            exit(1)
        else:
            self.language_pack = df

    def next_question(self) -> None:
        self.card_back.hide()
        self.card_front.hide()

        i = random.randint(0, len(self.language_pack) - 1)
        s = self.language_pack.iloc[i]

        self.card_back.update(text=s["translation"])
        self.card_front.update(text=s["english"])

        self.card_back.show()

    def click_handler(self):
        if self.card_status:
            self.card_back.hide()
            self.card_front.show()
            self.card_status = False
        else:
            self.card_front.hide()
            self.card_back.show()
            self.card_status = True
