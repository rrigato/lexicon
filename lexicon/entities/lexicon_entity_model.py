from typing import Optional


class AppConfig():
    """storing application configuration"""
    def __init__(
        self,
        audio_deck_name: Optional[str] = None,
        audio_note_template_name: Optional[str] = None,
        audio_vocab_card_audio_column_number: Optional[int] = None,
        audio_vocab_card_due_date: Optional[int] = None,
        llm_api_key: Optional[str] = None,
        reading_deck_name: Optional[str] = None,
        reading_note_template_name: Optional[str] = None,
        reading_vocab_card_audio_column_number: Optional[int] = None,
        reading_vocab_card_due_date: Optional[int] = None
    ):
        """Initialize all attributes to None"""
        self.audio_deck_name = audio_deck_name
        self.audio_note_template_name = audio_note_template_name
        self.audio_vocab_card_audio_column_number = audio_vocab_card_audio_column_number
        self.audio_vocab_card_due_date = audio_vocab_card_due_date
        self.llm_api_key = llm_api_key
        self.reading_deck_name = reading_deck_name
        self.reading_note_template_name = reading_note_template_name
        self.reading_vocab_card_audio_column_number = reading_vocab_card_audio_column_number
        self.reading_vocab_card_due_date = reading_vocab_card_due_date

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
    def audio_vocab_card_audio_column_number(self) -> Optional[int]:
        return(self._audio_vocab_card_audio_column_number)

    @audio_vocab_card_audio_column_number.setter
    def audio_vocab_card_audio_column_number(
        self,
        audio_vocab_card_audio_column_number: Optional[int]
    ):
        if type(audio_vocab_card_audio_column_number) not in (
            int, type(None)):
            raise TypeError(
                "AppConfig - audio_vocab_card_audio_column_number datatype " +
                "must be a int or None"
            )
        self._audio_vocab_card_audio_column_number = audio_vocab_card_audio_column_number

    @property
    def audio_vocab_card_due_date(self) -> Optional[int]:
        return(self._audio_vocab_card_due_date)

    @audio_vocab_card_due_date.setter
    def audio_vocab_card_due_date(self, audio_vocab_card_due_date: Optional[int]):
        if type(audio_vocab_card_due_date) not in (
            int, type(None)):
            raise TypeError(
                "AppConfig - audio_vocab_card_due_date datatype " +
                "must be a int or None"
            )
        self._audio_vocab_card_due_date = audio_vocab_card_due_date

    @property
    def llm_api_key(self) -> Optional[str]:
        return(self._llm_api_key)

    @llm_api_key.setter
    def llm_api_key(self, llm_api_key: Optional[str]):
        if type(llm_api_key) not in (
            str, type(None)):
            raise TypeError(
                "AppConfig - llm_api_key datatype " +
                "must be a str or None"
            )
        self._llm_api_key = llm_api_key

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

    @property
    def reading_vocab_card_audio_column_number(self) -> Optional[int]:
        return(self._reading_vocab_card_audio_column_number)

    @reading_vocab_card_audio_column_number.setter
    def reading_vocab_card_audio_column_number(
        self,
        reading_vocab_card_audio_column_number: Optional[int]
    ):
        if type(reading_vocab_card_audio_column_number) not in (
            int, type(None)):
            raise TypeError(
                "AppConfig - reading_vocab_card_audio_column_number datatype " +
                "must be a int or None"
            )
        self._reading_vocab_card_audio_column_number = reading_vocab_card_audio_column_number

    @property
    def reading_vocab_card_due_date(self) -> Optional[int]:
        return(self._reading_vocab_card_due_date)

    @reading_vocab_card_due_date.setter
    def reading_vocab_card_due_date(self, reading_vocab_card_due_date: Optional[int]):
        if type(reading_vocab_card_due_date) not in (
            int, type(None)):
            raise TypeError(
                "AppConfig - reading_vocab_card_due_date datatype " +
                "must be a int or None"
            )
        self._reading_vocab_card_due_date = reading_vocab_card_due_date

class FlashCard():
    """Represents a flash car in a spaced repition system"""
    def __init__(
            self,
            anki_card_id: Optional[int] = None,
            anki_note_id: Optional[int] = None,
        ):
        """Initialize all attributes to None"""
        self.anki_card_id = anki_card_id
        self.anki_note_id = anki_note_id
        self.english_definition = None
        self.front_text = None
        self.hiragana_text = None
        self.kanji_text = None
        self.note_type = None

    @property
    def anki_card_id(self) -> Optional[int]:
        """each note can have multiple cards
        that each have a unique id"""
        return(self._anki_card_id)

    @anki_card_id.setter
    def anki_card_id(self, anki_card_id: Optional[int]):
        if type(anki_card_id) not in (
            int, type(None)):
            raise TypeError(
                "FlashCard - anki_card_id datatype " +
                "must be a int or None"
            )
        self._anki_card_id = anki_card_id

    @property
    def anki_note_id(self) -> Optional[int]:
        """Unique identifier for the flash card in the Anki database"""
        return(self._anki_note_id)

    @anki_note_id.setter
    def anki_note_id(self, anki_note_id: Optional[int]):
        if type(anki_note_id) not in (
            int, type(None)):
            raise TypeError(
                "FlashCard - anki_note_id datatype " +
                "must be a int or None"
            )
        self._anki_note_id = anki_note_id

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
        vocab_to_create: Optional[str] = None,
        word_definition: Optional[str] = None,
    ):
        """Initialize all attributes to None"""
        self.hiragana_text = hiragana_text
        self.vocab_to_create = vocab_to_create
        self.word_definition = word_definition


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

    @property
    def word_definition(self) -> Optional[str]:
        return(self._word_definition)

    @word_definition.setter
    def word_definition(self, word_definition: Optional[str]):
        if type(word_definition) not in (
            str, type(None)):
            raise TypeError(
                "JapaneseVocabRequest - word_definition datatype " +
                "must be a str or None"
            )
        self._word_definition = word_definition

