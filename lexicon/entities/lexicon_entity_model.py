from typing import Optional


class FlashCard():
    """Represents a flash car in a spaced repition system"""
    def __init__(self):
        """Initialize all attributes to None"""
        self.front_text = None
        self.note_type = None

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

    @property
    def note_type(self) -> Optional[str]:
        return(self._note_type)

    @note_type.setter
    def note_type(self, note_type: Optional[str]):
        if type(note_type) not in (
            str, type(None)):
            raise TypeError(
                "MessageBoardPost - note_type datatype " +
                "must be a str or None"
            )
        self._note_type = note_type
