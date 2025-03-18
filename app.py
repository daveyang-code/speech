import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Initialize conversation history
conversation_history = []


def listen_to_microphone():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    mic = sr.Microphone(device_index=0)
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, the service is down.")
            return None


def generate_response(prompt):
    global conversation_history

    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": prompt})

    # Ensure the conversation history only keeps the last 10 messages
    if len(conversation_history) > 10:
        conversation_history = conversation_history[-10:]

    # Generate a response using the conversation history
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=conversation_history, max_tokens=150
    )

    # Extract the assistant's response
    assistant_response = response.choices[0].message.content

    # Add the assistant's response to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response


def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # Play the audio


def ai_assistant():
    while True:
        text = listen_to_microphone()
        if text:
            response = generate_response(text)
            print(f"AI: {response}")
            speak(response)


if __name__ == "__main__":
    ai_assistant()
