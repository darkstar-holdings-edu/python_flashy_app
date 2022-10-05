from tkinter import Button, Tk
import pandas as pd

from .config import BACKGROUND_COLOR
from .components import AppButton, Card

APP_NAME = "Flashy"
LANGUAGE_DATA_PATH = "data"


class App(Tk):
    language: str
    language_pack: pd.DataFrame

    words: pd.DataFrame = pd.DataFrame()
    word_weights: list[float] = []

    card: Card

    def __init__(self, language: str) -> None:
        super().__init__()

        self.language = language
        self.language_pack = self.load_language_pack()
        self.words = self.language_pack.iloc[:10]
        self.word_weights = [0.5 for _ in range(len(self.words))]

        self.load_user_interface()

    def load_user_interface(self) -> None:
        self.geometry("900x700")
        self.title(APP_NAME)
        self.config(padx=50, pady=50, background=BACKGROUND_COLOR)

        self.card = Card()
        AppButton(
            filename="assets/wrong.png",
            handler=self.wrong_handler,
        ).place(x=200, y=580, anchor="center")

        AppButton(
            filename="assets/right.png",
            handler=self.right_handler,
        ).place(x=575, y=580, anchor="center")

        Button(text="Reveal", command=self.click_handler).place(x=300, y=550)
        Button(text="Next", command=self.next_question).place(x=400, y=550)

        self.next_question()

    def load_language_pack(self) -> pd.DataFrame:
        try:
            df = pd.read_csv("/".join([LANGUAGE_DATA_PATH, f"{self.language}.csv"]))
        except FileNotFoundError:
            print(f"Invalid language pack: {self.language}")
            exit(1)
        else:
            self.language_pack = df

        return df

    def next_question(self) -> None:
        question = self.words.sample(
            n=1,
            weights=self.word_weights,
            replace=True,
        ).iloc[0]
        self.card.update(
            front_text=question["translation"],
            back_text=question["english"],
        )

        if self.card.is_flipped:
            self.card.flip()

    def click_handler(self) -> None:
        self.card.flip()

    def wrong_handler(self) -> None:
        print("Wrong")

    def right_handler(self) -> None:
        print("right")
