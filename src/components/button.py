from tkinter import Button, PhotoImage
from typing import Callable

from ..config import BACKGROUND_COLOR


class AppButton(Button):
    image: PhotoImage

    def __init__(self, filename: str, handler: Callable[[], None]) -> None:
        super().__init__()
        self.image = PhotoImage(file=filename)
        self.config(
            image=self.image,
            command=handler,
            highlightthickness=0,
            highlightbackground=BACKGROUND_COLOR,
            relief="flat",
            takefocus=False,
        )
