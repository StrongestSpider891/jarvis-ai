import openai
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

class AICore:
    def __init__(self):
        """Initialize the AI core with OpenAI API"""
        openai.api_key = OPENAI_API_KEY
        self.conversation_history = []
    
    def get_response(self, user_input):
        """Get AI response to user input"""
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=self.prepare_messages(),
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            
            # Extract response text
            assistant_message = response['choices'][0]['message']['content'].strip()
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except openai.error.AuthenticationError:
            return "Authentication failed. Please check your API key."
        except openai.error.APIError as e:
            return f"API Error: {str(e)}"
    
    def prepare_messages(self):
        """Prepare messages with system prompt for conversation"""
        system_prompt = {
            "role": "system",
            "content": "You are JARVIS, an advanced AI assistant. You are helpful, polite, and concise in your responses. Keep responses brief and natural for voice interaction."
        }
        
        return [system_prompt] + self.conversation_history[-10:]  # Keep last 10 messages for context
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
