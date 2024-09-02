from typing import Optional


class FlashCard():
    """Represents a flash car in a spaced repition system"""
    def __init__(self):
        """Initialize all attributes to None"""
        self.flash_card_type = None
        self.front_text = None

    @property
    def flash_card_type(self) -> Optional[str]:
        return(self._flash_card_type)

    @flash_card_type.setter
    def flash_card_type(self, flash_card_type: Optional[str]):
        if type(flash_card_type) not in (
            str, type(None)):
            raise TypeError(
                "MessageBoardPost - flash_card_type datatype " +
                "must be a str or None"
            )
        self._flash_card_type = flash_card_type

    @property
    def front_text(self) -> Optional[str]:
        return(self._front_text)

    @front_text.setter
    def front_text(self, front_text: Optional[str]):
        if type(front_text) not in (
            str, type(None)):
            raise TypeError(
                "MessageBoardPost - front_text datatype " +
                "must be a str or None"
            )
        self._front_text = front_text
