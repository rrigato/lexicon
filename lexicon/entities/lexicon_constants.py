LLM_MODEL_TEMPERATURE = 0
LLM_SYSTEM_PROMPT = (
    "You are a helpful assistant that provides "
    "concise English definitions for Japanese words."
    "Only provide the definition of the word, no other text."
    "If the word has multiple definitions, provide all of them."
    "If the word has multiple definitions, separate them with a comma."
    "Only provide a definition if it is commonly used in Japanese."
    "If you are not sure about the definition, say 'unknown'."
)
NOTE_FIELD_OFFSET = -1
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_LLM_MODEL = "gpt-4.1"