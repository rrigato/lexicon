from lexicon.entities.lexicon_entity_model import AppConfig, JapaneseVocabRequest

def load_api_definition(
    app_config: AppConfig,
    japanese_vocab_request: JapaneseVocabRequest
) -> JapaneseVocabRequest:
    """
    Returns a new JapaneseVocabRequest object where only
    the word_definition is populated
    """
    return JapaneseVocabRequest(
        word_definition="test_word_definition"
    )
