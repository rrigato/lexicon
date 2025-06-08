import json
import logging
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from lexicon.entities.lexicon_constants import LLM_MODEL_TEMPERATURE, OPENAI_API_URL, OPENAI_LLM_MODEL
from lexicon.entities.lexicon_entity_model import AppConfig, JapaneseVocabRequest

def load_api_definition(
    app_config: AppConfig,
    japanese_vocab_request: JapaneseVocabRequest
) -> JapaneseVocabRequest:
    """
    Returns a new JapaneseVocabRequest object where only
    the word_definition is populated from an OpenAI API call
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {app_config.llm_api_key}"
    }

    prompt = f"Provide a concise English definition for the Japanese word: {japanese_vocab_request.vocab_to_create}"

    data = {
        "model": OPENAI_LLM_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that provides concise English definitions for Japanese words."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100,
        "temperature": LLM_MODEL_TEMPERATURE
    }

    request = Request(
        OPENAI_API_URL,
        data=json.dumps(data).encode(),
        headers=headers,
        method="POST"
    )

    logging.info(f"load_api_definition - beginning api call")
    
    try:
        with urlopen(request) as response:
            response_data = json.loads(response.read().decode())
            logging.info(f"response_data: {response_data}")
            word_definition = response_data[
                "choices"
            ][0]["message"]["content"]

            return JapaneseVocabRequest(
                word_definition=word_definition
            )
    except HTTPError as e:
        logging.error(f"Error: {e}")
        raise e

if __name__ == "__main__":
    api_definition = load_api_definition(
        AppConfig(
            llm_api_key=os.getenv("anki_openai_key")
        ),
        JapaneseVocabRequest(
            vocab_to_create="洗脳"
        )
    )
    print(api_definition.word_definition)