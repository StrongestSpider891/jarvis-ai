import pyttsx3
import speech_recognition as sr
from config import VOICE_RATE, VOICE_VOLUME, RECOGNITION_TIMEOUT

class VoiceHandler:
    def __init__(self):
        """Initialize text-to-speech and speech recognition engines"""
        # Text-to-Speech
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', VOICE_RATE)
        self.engine.setProperty('volume', VOICE_VOLUME)
        
        # Speech Recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
    
    def speak(self, text):
        """Convert text to speech and play it"""
        print(f"[JARVIS]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to microphone input and convert to text"""
        try:
            with self.microphone as source:
                print("[LISTENING...]")
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Listen for audio
                audio = self.recognizer.listen(source, timeout=RECOGNITION_TIMEOUT)
            
            # Recognize speech using Google Speech Recognition
            text = self.recognizer.recognize_google(audio)
            print(f"[USER]: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that. Could you please repeat?")
            return None
        
        except sr.RequestError as e:
            self.speak(f"Error accessing speech recognition service: {e}")
            return None
        
        except sr.WaitTimeoutError:
            self.speak("I didn't hear anything. Please try again.")
            return None
    
    def get_voices(self):
        """Get available voices"""
        return self.engine.getProperty('voices')
    
    def set_voice(self, voice_id):
        """Set the voice by ID"""
        self.engine.setProperty('voice', voice_id)
