import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Voice Settings
VOICE_RATE = 150  # Speed of speech
VOICE_VOLUME = 1.0  # Volume level (0.0 to 1.0)

# AI Settings
MODEL_NAME = "gpt-3.5-turbo"
TEMPERATURE = 0.7
MAX_TOKENS = 150

# Recognition Settings
RECOGNITION_TIMEOUT = 10  # seconds
PHRASE_TIME_LIMIT = None

# Name/Wake word for the assistant
WAKE_WORD = "jarvis"
ASSISTANT_NAME = "Jarvis"
