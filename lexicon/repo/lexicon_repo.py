from copy import deepcopy
import logging
import os
from logging.handlers import RotatingFileHandler
import re
from time import strftime

import pykakasi
from lexicon.entities.lexicon_entity_model import AppConfig, FlashCard, JapaneseVocabRequest
from aqt import mw
from lexicon.usecase.lexicon_usecase import LearnJapaneseWordInterface



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

        current_collection = mw.col


        card_note_model = mw.col.models.by_name(
            app_config.audio_note_template_name
        )
        card_deck = mw.col.decks.by_name(app_config.audio_deck_name)

        logging.info(f"create_audio_vocab_card - found card_note_model and card_deck")

        new_note = mw.col.new_note(
            card_note_model
        )

        new_note.fields[0] = create_vocab_request.vocab_to_create
        new_note.fields[1] = create_vocab_request.hiragana_text

        logging.info(f"create_audio_vocab_card - populated new_note")


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
    ) -> bool:
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


        mw.col.add_note(new_note, card_deck["id"])

        logging.info(f"create_reading_vocab_card - saved new_note")

        return(True)

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
            audio_deck_name=user_defined_config["audio_vocab_deck_name"],
            audio_note_template_name=user_defined_config["audio_vocab_note_type"],
            audio_vocab_card_due_date=user_defined_config["audio_vocab_card_due_date"],
            reading_deck_name=user_defined_config["reading_vocab_deck_name"],
            reading_note_template_name=user_defined_config["reading_vocab_note_type"],
            reading_vocab_card_due_date=user_defined_config["reading_vocab_card_due_date"]
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
