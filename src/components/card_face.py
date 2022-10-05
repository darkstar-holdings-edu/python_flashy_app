from tkinter import Canvas, PhotoImage

from ..config import BACKGROUND_COLOR

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526


class CardFace:
    canvas: Canvas
    image: PhotoImage
    x_position: int = 0
    y_position: int = 0
    label_id: int

    def __init__(self, image: str, text: str, text_color: str) -> None:
        self.image = PhotoImage(file=image)

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
            fill=text_color,
            font=("Helvetica", 30, "normal italic"),
        )

        self.label_id = canvas.create_text(
            380,
            300,
            text="DEFAULT_TEXT",
            fill=text_color,
            font=("Helvetica", 45, "bold"),
        )

        self.canvas = canvas

    def update(self, text: str) -> None:
        self.canvas.itemconfig(self.label_id, text=text)

    def show(self) -> None:
        self.canvas.place(x=self.x_position, y=self.y_position)

    def hide(self) -> None:
        self.canvas.place_forget()
