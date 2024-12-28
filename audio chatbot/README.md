# Mic-Enabled Chatbot Project: Converse Naturally with Python!

This project demonstrates a simple chatbot that allows users to interact using voice input and receive audio responses. 

**Project Functionality**

* **Workflow:**

  ![download](https://github.com/user-attachments/assets/b6aeea98-f1d8-4627-9598-8a1a58b0d99d)

* **Steps:**
    1. **Speech Recognition:** Capture user audio input using the microphone.
    2. **Text Conversion:** Convert the captured audio to text using the Google Text-to-Speech (gTTS) library.
    3. **API Interaction:** Send the converted text to the Gemini API for processing and generating a response.
    4. **Speech Synthesis:** Convert the API response back into audio using gTTS.
    5. **Audio Playback:** Play the synthesized audio response to the user.

**Requirements**

* **Libraries:**
    * `playsound`
    * `speech_recognition`
    * `gtts` 
    * `google-generativeai`

* **Installation:**
   ```bash
   pip install playsound speech_recognition gtts google-generativeai

