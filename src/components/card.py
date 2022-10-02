from tkinter import Canvas, PhotoImage

from ..config import BACKGROUND_COLOR

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526


class Card:
    canvas: Canvas
    image: PhotoImage
    x_position: int
    y_position: int
    label_id: int

    def __init__(
        self,
        image: str,
        text: str,
        color: str,
        x_pos: int = 0,
        y_pos: int = 0,
    ) -> None:
        self.image = PhotoImage(file=image)
        self.x_position = x_pos
        self.y_position = y_pos

        canvas = Canvas(
            width=self.image.width(),
            height=self.image.height(),
            background=BACKGROUND_COLOR,
            highlightthickness=0,
        )

        canvas.create_image(
            self.image.width() // 2,
            self.image.height() // 2,
            image=self.image,
        )

        canvas.create_text(
            380,
            175,
            text=text,
            fill=color,
            font=("Helvetica", 30, "normal italic"),
        )

        self.label_id = canvas.create_text(
            380,
            300,
            text="Die Football",
            fill=color,
            font=("Helvetica", 45, "bold"),
        )

        self.canvas = canvas

    def update(self, text: str) -> None:
        self.canvas.itemconfig(self.label_id, text=text)

    def show(self) -> None:
        self.canvas.place(x=self.x_position, y=self.y_position)

    def hide(self) -> None:
        self.canvas.place_forget()
