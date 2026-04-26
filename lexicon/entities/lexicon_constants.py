LLM_AUDIO_PROMPT =(
    "Speak only the Japanese word. "
    "Use the provided text as the exact pronunciation target. "
    "Pronounce it naturally, as a native Japanese speaker would say it in everyday conversation. "
    "Say the whole word as one smooth utterance with no pauses or gaps between syllables, morae, or characters. "
    "Do not separate, spell out, or over-enunciate the sounds. "
    "Say the word at a natural conversational speed while still sounding clear and natural. "
    "Use normal Japanese pitch accent and rhythm. "
    "Do not spell it out, explain it, translate it, or add any extra words."
)
LLM_MODEL_TEMPERATURE = 0

LLM_SYSTEM_PROMPT = (
    "You are a helpful assistant that provides "
    "concise Japanese definitions for Japanese words."
    "Use short sentences and simple Japanese vocabulary."
    "Only provide the definition of the word, no other text."
    "If the word has multiple definitions, provide all of them."
    "If the word has multiple definitions, separate them with a comma."
    "Only provide a definition if it is commonly used in Japanese."
    "If you are not sure about the definition, say 'unknown'."
)

NOTE_FIELD_OFFSET = -1
OPENAI_AUDIO_MODEL = "gpt-4o-mini-tts"
OPENAI_AUDIO_VOICE = "ash"
OPENAI_AUDIO_SPEED = 1.2
OPENAI_AUDIO_API_URL = "https://api.openai.com/v1/audio/speech"
OPENAI_API_URL = "https://api.openai.com/v1/responses"
OPENAI_LLM_MODEL = "gpt-5.4-mini"
OPENAI_LLM_REASONING_EFFORT = "none"
