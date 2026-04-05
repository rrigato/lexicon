import json
import logging
import os
from copy import deepcopy
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from lexicon.entities.lexicon_constants import (
    LLM_AUDIO_PROMPT,
    LLM_SYSTEM_PROMPT,
    OPENAI_AUDIO_API_URL,
    OPENAI_AUDIO_MODEL,
    OPENAI_AUDIO_VOICE,
    OPENAI_API_URL,
    OPENAI_LLM_MODEL,
)
from lexicon.entities.lexicon_entity_model import AppConfig, JapaneseVocabRequest, AudioConfig


def _audio_request_to_file(
    app_config: AppConfig,
    audio_config: AudioConfig,
    audio_request: Request,
    japanese_vocab_request: JapaneseVocabRequest,
) -> None:
    """Orchestrates api call and writes to a file


    """
    path_to_audio_file = os.path.join(
        audio_config.full_directory_path_to_write_file,
        audio_config.file_name
    )
    try:
        '''
        openai contract for audio endpoint:
        https://platform.openai.com/docs/api-reference/audio/create
        '''
        with urlopen(audio_request) as audio_response:
            logging.info(f"_audio_request_to_file - audio_response recieved")
            with open(
                path_to_audio_file, "wb"
            ) as audio_file:
                audio_file.write(audio_response.read())
                logging.info(f"_audio_request_to_file - audio_file written to {path_to_audio_file}")
    except HTTPError as e:
        logging.error(f"Error: {e}")
        raise e

def _encoded_audio_post_data(
    japanese_vocab_request: JapaneseVocabRequest,
) -> bytes:
    """Post body for speech endpoint"""
    audio_input = (
        "Original text: "
        f"{japanese_vocab_request.vocab_to_create}\n"
        "Hiragana reading: "
        f"{japanese_vocab_request.hiragana_text}\n"
        "Target spoken output: the Japanese word only"
    )

    return json.dumps({
        "input": audio_input,
        "instructions": LLM_AUDIO_PROMPT,
        "model": OPENAI_AUDIO_MODEL,
        "voice": OPENAI_AUDIO_VOICE,
    }).encode()

def _encoded_openapi_post_data(
    system_prompt: str,
    user_prompt: str,
) -> bytes:
    """
    Encodes the OpenAI API post data
    """
    return json.dumps({
        "model": OPENAI_LLM_MODEL,
        "input": f"{system_prompt}: {user_prompt}",
        "reasoning": {"effort": "low"},
    }).encode()

def _openai_api_request_headers(app_config: AppConfig) -> dict:
    """Returns a deepcopy of OpenAI API request headers"""

    return deepcopy({
        "Content-Type": "application/json",
        "Authorization": f"Bearer {app_config.llm_api_key}"
    })

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

    user_prompt = (
        "Provide a concise English definition "
        "for the Japanese word: "
        f"{japanese_vocab_request.vocab_to_create}"
    )

    request = Request(
        OPENAI_API_URL,
        data=_encoded_openapi_post_data(
            system_prompt=LLM_SYSTEM_PROMPT,
            user_prompt=user_prompt
        ),
        headers=_openai_api_request_headers(app_config),
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


def write_audio_to_file(
    app_config: AppConfig,
    audio_config: AudioConfig,
    japanese_vocab_request: JapaneseVocabRequest,
    ) -> None:
    """Loads the audio for japanese_vocab_request.vocab_to_create
    into the location specified by audio_config
    from the openai api
    """
    logging.info(f"write_audio_to_file - start forming api call")

    audio_request = Request(
        OPENAI_AUDIO_API_URL,
        data=_encoded_audio_post_data(
            japanese_vocab_request=japanese_vocab_request
        ),
        headers=_openai_api_request_headers(app_config),
        method="POST"
    )

    _audio_request_to_file(
        app_config=app_config,
        audio_config=audio_config,
        audio_request=audio_request,
        japanese_vocab_request=japanese_vocab_request
    )


if __name__ == "__main__":
    write_audio_to_file(
        AppConfig(
            llm_api_key=os.getenv("anki_openai_key")
        ),
        AudioConfig(
            file_name="manual_speech_test.mp3",
            full_directory_path_to_write_file="."
        ),
        JapaneseVocabRequest(
            vocab_to_create="愚痴る"
        )
    )
