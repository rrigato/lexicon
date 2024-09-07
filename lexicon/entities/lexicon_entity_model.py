from typing import Optional


class FlashCard():
    """Represents a flash car in a spaced repition system"""
    def __init__(self):
        """Initialize all attributes to None"""
        self.english_definition = None
        self.front_text = None
        self.note_type = None

    @property
    def english_definition(self) -> Optional[str]:
        """Definition of what the FlashCard is testing in English"""
        return(self._english_definition)

    @english_definition.setter
    def english_definition(self, english_definition: Optional[str]):
        if type(english_definition) not in (
            str, type(None)):
            raise TypeError(
                "FlashCard - english_definition datatype " +
                "must be a str or None"
            )
        self._english_definition = english_definition

    @property
    def front_text(self) -> Optional[str]:
        return(self._front_text)

    @front_text.setter
    def front_text(self, front_text: Optional[str]):
        if type(front_text) not in (
            str, type(None)):
            raise TypeError(
                "FlashCard - front_text datatype " +
                "must be a str or None"
            )
        self._front_text = front_text

    @property
    def hiragana_text(self) -> Optional[str]:
        """hiragana representation of kanji or katakana word"""
        return(self._hiragana_text)

    @hiragana_text.setter
    def hiragana_text(self, hiragana_text: Optional[str]):
        if type(hiragana_text) not in (
            str, type(None)):
            raise TypeError(
                "FlashCard - hiragana_text datatype " +
                "must be a str or None"
            )
        self._hiragana_text = hiragana_text

    @property
    def note_type(self) -> Optional[str]:
        return(self._note_type)

    @note_type.setter
    def note_type(self, note_type: Optional[str]):
        if type(note_type) not in (
            str, type(None)):
            raise TypeError(
                "FlashCard - note_type datatype " +
                "must be a str or None"
            )
        self._note_type = note_type
