from copy import deepcopy
import logging
import os
from logging.handlers import RotatingFileHandler
import re
from time import strftime

import pykakasi
from lexicon.entities.lexicon_entity_model import FlashCard, JapaneseVocabRequest
from aqt import mw

from lexicon.usecase.lexicon_usecase import LearnJapaneseWordInterface

def create_audio_vocab_card(
    flash_card_to_create: FlashCard
    ) -> None:
    """creates an audio flash card in external system
    """
    logging.info(f"create_audio_vocab_card - invocation begin")

    logging.info(f"create_audio_vocab_card - invocation end")
    return(None)


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
        backupCount=3
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
        Documentation for pykakasi convert, note it returns a list of dictionaries,
        assuming only one japanese word is passed in
        https://pykakasi.readthedocs.io/en/stable/api.html#api-documents-ref
        '''
        cloned_vocab_request.hiragana_text = pykakasi_instance.convert(
            cloned_vocab_request.vocab_to_create
        )[0]["hira"]

        logging.info(f"populate_hiragana_text - invocation end")

        return(cloned_vocab_request)