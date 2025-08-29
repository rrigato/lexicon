import json
import logging
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from lexicon.entities.lexicon_constants import LLM_MODEL_TEMPERATURE, LLM_SYSTEM_PROMPT, OPENAI_API_URL, OPENAI_LLM_MODEL
from lexicon.entities.lexicon_entity_model import AppConfig, JapaneseVocabRequest


def _encoded_openapi_post_data(
    user_prompt: str,
) -> bytes:
    """
    Encodes the OpenAI API post data
    """
    return json.dumps({
        "model": OPENAI_LLM_MODEL,
        "input": f"{LLM_SYSTEM_PROMPT}: {user_prompt}",
        "reasoning": {"effort": "low"},
    }).encode()

def _parse_openai_response(response_data: dict) -> str:
    """
    Parses the OpenAI API response

    Parameters
    ----------
    response_data : dict
        openai docs for response endpoint:
        https://platform.openai.com/docs/api-reference/responses/create
    """
    response_message = [
        message for message in response_data["output"]
        if message["type"] == "message"
    ]
    return response_message[0]["content"][0]["text"]


def automatically_generate_definition(
    app_config: AppConfig,
    japanese_vocab_request: JapaneseVocabRequest
) -> JapaneseVocabRequest:
    """
    Returns a new JapaneseVocabRequest object where only
    the word_definition is populated from an OpenAI API call
    """
    logging.info(f"automatically_generate_definition - start forming api call")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {app_config.llm_api_key}"
    }

    user_prompt = (
        "Provide a concise English definition "
        "for the Japanese word: "
        f"{japanese_vocab_request.vocab_to_create}"
    )

    request = Request(
        OPENAI_API_URL,
        data=_encoded_openapi_post_data(
            user_prompt=user_prompt
        ),
        headers=headers,
        method="POST"
    )

    logging.info(f"automatically_generate_definition - user_prompt: \n {user_prompt}")

    try:
        with urlopen(request) as response:
            response_data = json.loads(response.read().decode())
            logging.info(f"automatically_generate_definition - response_data: \n {response_data}")
            word_definition = _parse_openai_response(response_data)

            return JapaneseVocabRequest(
                word_definition=word_definition
            )
    except HTTPError as e:
        logging.error(f"Error: {e}")
        raise e

if __name__ == "__main__":
    api_definition = automatically_generate_definition(
        AppConfig(
            llm_api_key=os.getenv("anki_openai_key")
        ),
        JapaneseVocabRequest(
            vocab_to_create="洗脳"
        )
    )
    print(api_definition.word_definition)
