from .card_face import CardFace

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526


class Card:
    front: CardFace
    back: CardFace
    is_flipped: bool = False

    def __init__(self) -> None:
        self.front = CardFace(
            image="assets/card_back.png",
            text="Deutsch",
            text_color="white",
        )

        self.back = CardFace(
            image="assets/card_front.png",
            text="English",
            text_color="black",
        )

        self.front.show()

    def flip(self) -> None:
        if not self.is_flipped:
            self.front.hide()
            self.back.show()
            self.is_flipped = True
        else:
            self.back.hide()
            self.front.show()
            self.is_flipped = False

    def update(self, front_text: str, back_text: str) -> None:
        self.front.update(text=front_text)
        self.back.update(text=back_text)
