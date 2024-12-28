The code in the main.py file is a chatbot but takes mic input rather than typing on yout keyboard.
First you talk into your mic and then it sends the audio to the google servers using the gTTS library and converts it to text.
Then it sends the text to the gemini api which ouputs the response.
Lastly, it sends it back through the gTTS library and converts it into audio for the user to hear. 

requirements:

These are the required libraries you have to download to make the code work. (you can use your command prompt in windows or terminal in linux or macos)

pip install playsound
pip install speech_recognition
pip install gtts
pip install elevenlabs
pip install google-generativeai

After installing all the libraries, you can go on to run the code in your ide, text editor, or notebook of your choice. 
![Visual Representation Of The Processes](https://github.com/user-attachments/assets/13d7d19d-8321-4ed1-bc25-d5b0264281b0)