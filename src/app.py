from tkinter import Button, Tk
import pandas as pd

from .config import BACKGROUND_COLOR
from .components import AppButton, Card

APP_NAME = "Flashy"
LANGUAGE_DATA_PATH = "data"


class App(Tk):
    language: str
    language_pack: pd.DataFrame
    words: pd.DataFrame
    current_word: pd.Series

    card: Card

    def __init__(self, language: str) -> None:
        super().__init__()

        self.language = language
        self.language_pack = self.load_language_pack()
        self.words: pd.DataFrame = self.language_pack.iloc[:10]
        self.words.insert(3, "known", [0 for _ in range(len(self.words.index))])

        self.load_user_interface()
        self.next_question()

    def load_language_pack(self) -> pd.DataFrame:
        try:
            df = pd.read_csv("/".join([LANGUAGE_DATA_PATH, f"{self.language}.csv"]))
        except FileNotFoundError:
            print(f"Invalid language pack: {self.language}")
            exit(1)
        else:
            self.language_pack = df

        return df.sample(frac=1).reset_index(drop=True)

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

    def next_question(self) -> None:
        print(self.words)
        self.current_word = self.words[self.words["known"] == 0].iloc[0]
        self.card.update(
            front_text=self.current_word["translation"],
            back_text=self.current_word["english"],
        )

        if self.card.is_flipped:
            self.card.flip()

    def click_handler(self) -> None:
        self.card.flip()

    def wrong_handler(self) -> None:
        words = self.words.copy()
        words.loc[len(words)] = self.current_word.values.tolist()
        self.words = words.drop(self.current_word.name).reset_index(drop=True)

        self.next_question()

    def add_word(self) -> None:
        words = self.words.copy()
        new_word = self.language_pack.iloc[len(words) + 1]
        new_word["known"] = 0
        words.loc[len(self.words)] = new_word
        self.words = words

    def right_handler(self) -> None:
        self.words.iloc[[self.current_word.name], 3] = 1
        self.add_word()
        self.next_question()
