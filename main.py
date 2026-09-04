from voice_handler import VoiceHandler
from ai_core import AICore
from config import WAKE_WORD, ASSISTANT_NAME

class JARVIS:
    def __init__(self):
        """Initialize JARVIS AI Assistant"""
        self.voice = VoiceHandler()
        self.ai = AICore()
        self.running = True
    
    def greet(self):
        """Greet the user on startup"""
        greeting = f"Hello! I'm {ASSISTANT_NAME}, your personal AI assistant. How can I help you today?"
        self.voice.speak(greeting)
    
    def listen_for_wake_word(self):
        """Listen until wake word is detected"""
        while self.running:
            user_input = self.voice.listen()
            if user_input and WAKE_WORD in user_input:
                return True
        return False
    
    def handle_command(self, user_input):
        """Handle user command"""
        # Check for exit commands
        if any(word in user_input for word in ['exit', 'quit', 'bye', 'goodbye', 'stop']):
            self.voice.speak("Goodbye! It was nice talking to you.")
            self.running = False
            return False
        
        # Check for clear history command
        if any(word in user_input for word in ['clear', 'reset', 'forget']):
            self.ai.clear_history()
            self.voice.speak("Conversation history cleared.")
            return True
        
        # Get AI response
        response = self.ai.get_response(user_input)
        self.voice.speak(response)
        return True
    
    def run(self):
        """Main loop for JARVIS"""
        print(f"Starting {ASSISTANT_NAME}...")
        self.greet()
        
        while self.running:
            print(f"\nListening for wake word '{WAKE_WORD}'...")
            
            # Listen for wake word
            if self.listen_for_wake_word():
                self.voice.speak("I'm listening.")
                
                # Listen for command
                user_input = self.voice.listen()
                
                if user_input:
                    self.handle_command(user_input)
        
        print("JARVIS stopped.")

if __name__ == "__main__":
    jarvis = JARVIS()
    jarvis.run()
