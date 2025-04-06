import logging
import os
import re
from copy import deepcopy
from logging.handlers import RotatingFileHandler
import tempfile
from time import strftime
from typing import TYPE_CHECKING

import pykakasi
from aqt import mw
from gtts import gTTS

from lexicon.entities.lexicon_entity_model import (AppConfig, FlashCard,
                                                   JapaneseVocabRequest)
from lexicon.usecase.lexicon_usecase import LearnJapaneseWordInterface, audio_column_selector, reading_column_selector

if TYPE_CHECKING:
    from anki.decks import DeckDict
    from anki.models import NotetypeDict

def _obtain_audio_note_and_deck(
        app_config: AppConfig
    ) -> tuple["DeckDict", "NotetypeDict"]:
    card_note_model = mw.col.models.by_name(
        app_config.audio_note_template_name
    )
    card_deck = mw.col.decks.by_name(app_config.audio_deck_name)

    logging.info(f"create_audio_vocab_card - found card_note_model and card_deck")

    new_note = mw.col.new_note(
        card_note_model
    )

    return card_deck, new_note


def set_logger() -> None:
    """Set logger configuration
    https://github.com/abdnh/ankiutils/blob/master/src/ankiutils/log.py
    https://github.com/abdnh/anki-zim-reader/blob/master/src/consts.py#L4

    """
    lexicon_handler = RotatingFileHandler(
        filename=os.path.join(
            mw.addonManager.addonsFolder("lexicon"),
            "user_files",
            "lexicon_addon.log"
        ),
        maxBytes=3 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )


    lexicon_handler.setFormatter(logging.Formatter(
                fmt="%(levelname)s | %(asctime)s.%(msecs)03d" +
                strftime("%z") + " | %(message)s",
                datefmt="%Y-%m-%dT%H:%M:%S",
            )
    )
    lexicon_handler.setLevel(logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(lexicon_handler)

    return(None)


class FlashCardRepo(LearnJapaneseWordInterface):
    """"""
    @staticmethod
    def create_audio_vocab_card(
        app_config: AppConfig,
        create_vocab_request: JapaneseVocabRequest
    ) -> bool:
        """
        Invariants:
            - collection (mw.col) is loaded
        """
        logging.info(f"create_audio_vocab_card - invocation begin")


        card_deck, new_note = _obtain_audio_note_and_deck(app_config)

        new_note.fields[0] = create_vocab_request.vocab_to_create
        new_note.fields[1] = create_vocab_request.hiragana_text
        new_note.fields[3] = create_vocab_request.word_definition
        logging.info(f"create_audio_vocab_card - populated new_note")

        logging.info(
            f"create_audio_vocab_card - added mp3 file to Anki's"
             + " media collection"
        )

        media_filename = FlashCardRepo.make_mp3_for_anki(
            app_config,
            create_vocab_request
        )
        # Add a sound reference to the notes field
        new_note.fields[
            app_config.audio_vocab_card_audio_column_number
        ] = "[sound:{anki_media_file}]".format(
            anki_media_file=media_filename
        )

        logging.info(f"create_audio_vocab_card - cleaned up mp3 file")


        mw.col.add_note(new_note, card_deck["id"])

        logging.info(f"create_audio_vocab_card - saved new_note")


        return(
            FlashCard(
                anki_card_id=new_note.cards()[0].id,
                anki_note_id=new_note.id,
            )
        )

    @staticmethod
    def create_reading_vocab_card(
        create_vocab_request: JapaneseVocabRequest,
        app_config: AppConfig
    ) -> FlashCard:
        """Creates a new reading vocab card
        """
        logging.info(f"create_reading_vocab_card - invocation begin")

        card_note_model = mw.col.models.by_name(
            app_config.reading_note_template_name
        )
        card_deck = mw.col.decks.by_name(app_config.reading_deck_name)

        logging.info(f"create_reading_vocab_card - found card_note_model and card_deck")

        new_note = mw.col.new_note(
            card_note_model
        )

        new_note.fields[0] = create_vocab_request.vocab_to_create
        new_note.fields[1] = create_vocab_request.hiragana_text

        logging.info(f"create_reading_vocab_card - populated new_note")

        media_filename = FlashCardRepo.make_mp3_for_anki(
            app_config,
            create_vocab_request
        )
        # Add a sound reference to the notes field
        new_note.fields[
            app_config.reading_vocab_card_audio_column_number
        ] = "[sound:{anki_media_file}]".format(
            anki_media_file=media_filename
        )

        mw.col.add_note(new_note, card_deck["id"])

        logging.info(f"create_reading_vocab_card - saved new_note")

        return(
            FlashCard(
                anki_card_id=new_note.cards()[0].id,
                anki_note_id=new_note.id
            )
        )

    @staticmethod
    def is_only_japanese_characters(
        potential_japanese_input: str
    ) -> bool:
        """checks if the input string is only japanese characters
        """
        logging.info(f"is_only_japanese_characters - invocation begin")
        '''
        Unicode ranges for Japanese characters
        '''
        japanese_characters = re.compile(
            r"^[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF01-\uFF60\u3000-\u303F]+$"
        )

        japanese_character_count = len(
            re.findall(r"[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF01-\uFF60\u3000-\u303F]",
                       potential_japanese_input)
        )

        is_entirely_japanese = bool(japanese_characters.match(potential_japanese_input))

        logging.info(f"is_only_japanese_characters - invocation end")
        return(is_entirely_japanese)

    @staticmethod
    def make_mp3_for_anki(
        app_config: AppConfig,
        vocab_request: JapaneseVocabRequest
    ) -> str:
        """Creates an mp3 file for the vocab_request.vocab_to_create
        and returns the path to the sound file on the file system
        of the process
        """
        logging.info(f"make_mp3_for_anki - invocation begin")

        tts = gTTS(
            text=vocab_request.vocab_to_create,
            lang="ja"
        )
        temp_dir = tempfile.gettempdir()

        temp_path = os.path.join(
            temp_dir,
            vocab_request.vocab_to_create + ".mp3"
        )
        tts.save(temp_path)

        logging.info(
            f"make_mp3_for_anki - saved mp3 "
            + f"file to - {temp_path}"
        )

        media_filename = mw.col.media.add_file(temp_path)
        logging.info(
            f"make_mp3_for_anki - added mp3 file to Anki's"
             + " media collection"
        )


        logging.info(f"make_mp3_for_anki - cleaned up temp file")

        return(media_filename)

    @staticmethod
    def populate_hiragana_text(
        initial_vocab_request: JapaneseVocabRequest
    ) -> JapaneseVocabRequest:
        """Creates a new JapaneseVocabRequest where hiragana_text
        is populated from initial_vocab_request.vocab_to_create

        invariants:
            - initial_vocab_request.vocab_to_create
            is only one japanese word
        """
        logging.info(f"populate_hiragana_text - invocation begin")

        cloned_vocab_request = deepcopy(initial_vocab_request)

        pykakasi_instance = pykakasi.kakasi()


        '''
        Documentation for pykakasi convert,
        note it returns a list of dictionaries for all japanese words
        in the input string
        https://pykakasi.readthedocs.io/en/stable/api.html#api-documents-ref
        '''
        cloned_vocab_request.hiragana_text = pykakasi_instance.convert(
            cloned_vocab_request.vocab_to_create
        )[0]["hira"]

        logging.info(f"populate_hiragana_text - initial_vocab_request.vocab_to_create: {initial_vocab_request.vocab_to_create}")
        logging.info(f"populate_hiragana_text - cloned_vocab_request.hiragana_text: {cloned_vocab_request.hiragana_text}")

        return(cloned_vocab_request)

    @staticmethod
    def retrieve_app_config() -> AppConfig:
        """retrieves the app configuration
        """
        logging.info(f"retrieve_app_config - invocation begin")

        user_defined_config = mw.addonManager.getConfig(__name__)

        app_config = AppConfig(
            audio_deck_name=user_defined_config[
                "audio_vocab_deck_name"
            ],
            audio_note_template_name=user_defined_config[
                "audio_vocab_note_type"
            ],
            audio_vocab_card_due_date=user_defined_config[
                "audio_vocab_card_due_date"
            ],
            audio_vocab_card_audio_column_number=user_defined_config[
                "audio_vocab_card_audio_column_number"
            ],
            reading_deck_name=user_defined_config[
                "reading_vocab_deck_name"
            ],
            reading_note_template_name=user_defined_config[
                "reading_vocab_note_type"
            ],
            reading_vocab_card_due_date=user_defined_config[
                "reading_vocab_card_due_date"
            ],
            reading_vocab_card_audio_column_number=user_defined_config[
                "reading_vocab_card_audio_column_number"
            ]
        )

        app_config.audio_vocab_card_audio_column_number = (
            audio_column_selector(
                app_config
            )
        )

        app_config.reading_vocab_card_audio_column_number = (
            reading_column_selector(
                app_config
            )
        )

        logging.info(f"retrieve_app_config - invocation end")
        return(app_config)

    @staticmethod
    def set_flash_card_due_date_in_embeded_application(
        days_from_today: int,
        flash_card: FlashCard
    ) -> None:
        """Sets the due date for the flash_card in
        the external spaced repetition system SRS application Anki
        to days_from_today
        """
        logging.info(f"set_flash_card_due_date_in_embeded_application - invocation begin")

        if days_from_today is None:
            logging.info(f"set_flash_card_due_date_in_embeded_application - due date not set")
            return(None)

        mw.col.sched.set_due_date(
            card_ids=[flash_card.anki_card_id],
            days=str(days_from_today)
        )

        logging.info(f"set_flash_card_due_date_in_embeded_application - invocation end")
