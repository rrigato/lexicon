from typing import Optional


class AppConfig():
    """storing application configuration"""
    def __init__(
        self,
        audio_deck_name: Optional[str] = None,
        audio_note_template_name: Optional[str] = None,
        reading_deck_name: Optional[str] = None,
        reading_note_template_name: Optional[str] = None
    ):
        """Initialize all attributes to None"""
        self.audio_deck_name = audio_deck_name
        self.audio_deck_name = audio_deck_name
        self.reading_note_template_name = reading_note_template_name
        self.reading_note_template_name = reading_note_template_name


    @property
    def audio_deck_name(self) -> Optional[str]:
        return(self._audio_deck_name)

    @audio_deck_name.setter
    def audio_deck_name(self, audio_deck_name: Optional[str]):
        if type(audio_deck_name) not in (
            str, type(None)):
            raise TypeError(
                "AppConfig - audio_deck_name datatype " +
                "must be a str or None"
            )
        self._audio_deck_name = audio_deck_name

    @property
    def audio_note_template_name(self) -> Optional[str]:
        return(self._audio_note_template_name)
    @audio_note_template_name.setter
    def audio_note_template_name(self, audio_note_template_name: Optional[str]):
        if type(audio_note_template_name) not in (
            str, type(None)):
            raise TypeError(
                "AppConfig - audio_note_template_name datatype " +
                "must be a str or None"
            )
        self._audio_note_template_name = audio_note_template_name

    @property
    def reading_deck_name(self) -> Optional[str]:
        return(self._reading_deck_name)

    @reading_deck_name.setter
    def reading_deck_name(self, reading_deck_name: Optional[str]):
        if type(reading_deck_name) not in (
            str, type(None)):
            raise TypeError(
                "AppConfig - reading_deck_name datatype " +
                "must be a str or None"
            )
        self._reading_deck_name = reading_deck_name

    @property
    def reading_note_template_name(self) -> Optional[str]:
        return(self._reading_note_template_name)
    @reading_note_template_name.setter
    def reading_note_template_name(self, reading_note_template_name: Optional[str]):
        if type(reading_note_template_name) not in (
            str, type(None)):
            raise TypeError(
                "AppConfig - reading_note_template_name datatype " +
                "must be a str or None"
            )
        self._reading_note_template_name = reading_note_template_name



class FlashCard():
    """Represents a flash car in a spaced repition system"""
    def __init__(self):
        """Initialize all attributes to None"""
        self.english_definition = None
        self.front_text = None
        self.hiragana_text = None
        self.kanji_text = None
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
    def kanji_text(self) -> Optional[str]:
        """hiragana representation of kanji or katakana word"""
        return(self._kanji_text)

    @kanji_text.setter
    def kanji_text(self, kanji_text: Optional[str]):
        if type(kanji_text) not in (
            str, type(None)):
            raise TypeError(
                "FlashCard - kanji_text datatype " +
                "must be a str or None"
            )
        self._kanji_text = kanji_text

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


class JapaneseVocabRequest():
    """Valid required input to create FlashCard of type Japanese"""
    def __init__(
        self,
        hiragana_text: Optional[str] = None,
        vocab_to_create: Optional[str] = None
    ):
        """Initialize all attributes to None"""
        self.hiragana_text = hiragana_text
        self.vocab_to_create = vocab_to_create


    @property
    def hiragana_text(self) -> Optional[str]:
        """hiragana representation of kanji or katakana word"""
        return(self._hiragana_text)

    @hiragana_text.setter
    def hiragana_text(self, hiragana_text: Optional[str]):
        if type(hiragana_text) not in (
            str, type(None)):
            raise TypeError(
                "JapaneseVocabRequest - hiragana_text datatype " +
                "must be a str or None"
            )
        self._hiragana_text = hiragana_text

    @property
    def vocab_to_create(self) -> Optional[str]:
        return(self._vocab_to_create)
    @vocab_to_create.setter
    def vocab_to_create(self, vocab_to_create: Optional[str]):
        if type(vocab_to_create) not in (
            str, type(None)):
            raise TypeError(
                "JapaneseVocabRequest - vocab_to_create datatype " +
                "must be a str or None"
            )
        self._vocab_to_create = vocab_to_create

