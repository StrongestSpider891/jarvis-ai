# JARVIS AI Assistant

A voice-activated AI assistant inspired by the JARVIS system from Iron Man. This project combines speech recognition, natural language processing, and text-to-speech to create an interactive voice assistant powered by OpenAI's GPT models.

## Features

✨ **Voice Interaction**
- Real-time speech recognition using Google Speech Recognition API
- Natural text-to-speech responses using pyttsx3
- Wake word detection ("Jarvis") for hands-free activation

🤖 **AI-Powered Responses**
- Integration with OpenAI's GPT-3.5-turbo model
- Conversational memory to maintain context across interactions
- Customizable personality and response tone

⚙️ **Configurable Settings**
- Adjustable voice speed and volume
- Customizable wake word and assistant name
- Easy-to-modify AI parameters (temperature, max tokens, etc.)

## Project Structure

```
jarvis-ai/
├── main.py                # Main application entry point
├── config.py              # Configuration settings
├── ai_core.py            # OpenAI integration module
├── voice_handler.py      # Speech recognition and TTS module
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Prerequisites

- Python 3.8 or higher
- Microphone and speaker
- OpenAI API key
- PortAudio (for PyAudio on some systems)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/StrongestSpider891/jarvis-ai.git
   cd jarvis-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. **Start the assistant**
   ```bash
   python main.py
   ```

2. **Interact with JARVIS**
   - Wait for "Listening for wake word 'jarvis'..."
   - Say "Jarvis" to activate
   - After hearing "I'm listening.", speak your command or question
   - JARVIS will process and respond with voice

3. **Exit commands**
   - Say: "exit", "quit", "bye", "goodbye", or "stop"

4. **Clear history**
   - Say: "clear", "reset", or "forget" to clear conversation history

## Configuration

Edit `config.py` to customize:

```python
VOICE_RATE = 150           # Speech speed (words per minute)
VOICE_VOLUME = 1.0         # Volume level (0.0-1.0)
WAKE_WORD = "jarvis"       # Wake word to activate assistant
MODEL_NAME = "gpt-3.5-turbo"  # OpenAI model
TEMPERATURE = 0.7          # Response creativity (0-1)
MAX_TOKENS = 150           # Maximum response length
RECOGNITION_TIMEOUT = 10   # Listening timeout in seconds
```

## Modules

### `main.py`
The main application loop that orchestrates the voice interaction, listening for wake words, and processing commands.

**Key Methods:**
- `greet()` - Greets the user on startup
- `listen_for_wake_word()` - Waits for the wake word
- `handle_command()` - Processes user commands
- `run()` - Main application loop

### `voice_handler.py`
Handles all voice-related operations including speech recognition and text-to-speech.

**Key Methods:**
- `speak(text)` - Converts text to speech
- `listen()` - Converts speech to text
- `set_voice(voice_id)` - Changes the voice

### `ai_core.py`
Manages OpenAI API integration and conversation history.

**Key Methods:**
- `get_response(user_input)` - Gets AI response to user input
- `prepare_messages()` - Prepares conversation context
- `clear_history()` - Clears conversation history

### `config.py`
Contains all configuration settings and environment variables.

## Troubleshooting

**Issue: "Could not find PyAudio"**
- Install PortAudio: `brew install portaudio` (macOS) or `apt-get install portaudio19-dev` (Linux)
- Then reinstall PyAudio: `pip install --upgrade pyaudio`

**Issue: "API Key not found"**
- Ensure `.env` file exists in the project root
- Verify `OPENAI_API_KEY` is set correctly in `.env`
- Check that `python-dotenv` is installed: `pip install python-dotenv`

**Issue: Microphone not detected**
- Check system audio settings
- Test microphone with system tools before running JARVIS
- Verify microphone permissions in system settings

**Issue: Poor speech recognition**
- Reduce background noise
- Speak clearly and at a normal pace
- Adjust `RECOGNITION_TIMEOUT` in `config.py`
- Try adjusting microphone volume

## Requirements

```
SpeechRecognition==3.10.0
pyttsx3==2.90
pyaudio==0.2.13
openai==1.3.0
python-dotenv==1.0.0
requests==2.31.0
numpy==1.24.3
torch==2.0.0
transformers==4.30.0
```

## API Costs

This project uses OpenAI's API which may incur costs. Monitor your API usage at [OpenAI's dashboard](https://platform.openai.com/account/usage/overview).

## Future Enhancements

- [ ] Integration with smart home devices
- [ ] Task automation and scheduling
- [ ] Local command execution
- [ ] Integration with calendar and email
- [ ] Custom wake word training
- [ ] Offline mode for basic commands
- [ ] Web interface for settings
- [ ] Support for multiple languages

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

## Disclaimer

This is a personal project inspired by JARVIS from Marvel. It's not affiliated with Marvel Studios or any commercial entity. Use responsibly and ensure you comply with all relevant laws and regulations regarding voice recording and AI usage.

## Support

If you encounter any issues, please:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the configuration in `config.py`
3. Check your OpenAI API status and credits
4. Open an issue on GitHub with detailed error messages

---

**Enjoy your personal AI assistant!** 🚀
