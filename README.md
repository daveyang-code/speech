# AI Voice Assistant

A Python-based voice assistant that listens to your voice, processes your requests using OpenAI and responds verbally using text-to-speech technology.

# Features
- Voice Recognition: Listens to your microphone input using speech recognition
- AI Conversation: Maintains context with conversation history (last 10 messages)
- Voice Response: Speaks responses using Google's Text-to-Speech (gTTS)

# Installation
```
pip install speechrecognition openai gtts python-dotenv
```

```
sudo apt install mpg321
```

Create a ```.env``` file in the project directory with:
```
OPENAI_API_KEY=your_api_key_here
```
