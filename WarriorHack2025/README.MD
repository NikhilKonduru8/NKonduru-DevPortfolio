# The Utterly Impractical Sensory Swap Device

For this hackathon, we embraced the challenge of creating something deliberately impractical. Our hilariously misguided creation is a device that includes an Arduino-based "Blind Visor" (bvisor) designed to display distance visually, and a Raspberry Pi-based "Deaf Buzzer" (dbuzzer) intended to convey spoken words as audible Morse code beeps. We then, in the spirit of utter uselessness, swapped their intended purposes.

## Project Goal

To fulfill the hackathon's call for impracticality, we crafted a device where the blind can "see" distance readings on an LCD screen, and the deaf can "hear" spoken words translated into Morse code beeps. The result is the wonderfully useless combination of the bvisor and the dbuzzer, precisely as described.

## Components and Functionality

**Blind Visor (bvisor - Arduino):**

* **Arduino:** This microcontroller acts as the brain, executing the code to control the sensor and display.
* **Distance Sensor (Ultrasonic):** This sensor emits ultrasonic sound waves and measures the time it takes for the echo to return, calculating the distance to the nearest object.
    * **Function:** The `trigPin` sends out the ultrasonic pulse, and the `echoPin` listens for the returning echo. The `pulseIn()` function measures the duration of the echo. This duration is then used to calculate the distance in centimeters and inches using specific formulas based on the speed of sound.
* **Potentiometer:** (Although not explicitly used in the provided code, it was likely intended for some form of adjustment or was part of the initial setup).
* **LCD Display (16x2):** This display shows text output.
    * **Function:** The `LiquidCrystal` library is used to communicate with the LCD. The `lcd.begin(16, 2)` line initializes the display with 16 columns and 2 rows. The `lcd.setCursor()` function sets the position for the text, and `lcd.print()` displays the distance values along with units.
* **9V Battery:** Provides portable power to the Arduino and its components.

**Libraries Needed (Arduino):**

* `LiquidCrystal.h`: This library is essential for controlling the LCD display. You need to include it at the beginning of your Arduino sketch.

**Deaf Buzzer (dbuzzer - Raspberry Pi):**

* **Raspberry Pi:** A small single-board computer that runs the Python code for speech recognition and Morse code conversion.
* **PiSugar:** A power solution designed for portable use of the Raspberry Pi.
* **Buzzer:** An electronic component that produces a beeping sound when a voltage is applied to it.
    * **Function:** The `gpiozero.Buzzer(17)` line initializes the buzzer connected to GPIO pin 17 of the Raspberry Pi. The `buzzer.on()` and `buzzer.off()` functions control the buzzer's state. The `sleep()` function from the `time` library controls the duration of the beeps and pauses, creating the Morse code patterns.
* **Microphone:** A device that captures sound waves and converts them into electrical signals. The built-in microphone or an external USB microphone can be used.
    * **Function:** The `speech_recognition` library uses the microphone as a `source` to record audio.
* **Speech Recognition Library (`speech_recognition`):** This Python library allows the Raspberry Pi to convert spoken audio into text using various speech recognition services (in this case, Google Speech Recognition).
    * **Function:** The `sr.Recognizer()` creates a recognizer object. The `r.listen(source)` function records audio from the microphone. The `r.recognize_google(audio)` function sends the audio data to Google's speech recognition service and returns the recognized text.
* **GPIO Zero Library (`gpiozero`):** This Python library provides a simple interface for controlling hardware components connected to the Raspberry Pi's GPIO pins, such as the buzzer.

**Libraries Needed (Python):**

* `speech_recognition`: This library is necessary for performing speech-to-text conversion. You can install it using `pip install SpeechRecognition`.
* `gpiozero`: This library simplifies controlling GPIO components. You can install it using `pip install gpiozero`.
* `time`: This built-in Python module provides time-related functions, specifically `sleep()` for controlling the duration of the Morse code beeps and pauses.

## Code Structure and Functionality

**bvisor (Arduino - `naked_bvisor.ino`):**

* Includes the `LiquidCrystal.h` library.
* Creates an `lcd` object, defining the Arduino pins connected to the LCD.
* Defines constants for the `trigPin` and `echoPin` connected to the ultrasonic sensor.
* In the `setup()` function:
    * Initializes the LCD with `lcd.begin(16, 2)`.
    * Sets the `trigPin` as an output and the `echoPin` as an input.
* In the `loop()` function:
    * Sends a short ultrasonic pulse by setting `trigPin` HIGH for 10 microseconds.
    * Measures the duration of the returning echo using `pulseIn(echoPin, HIGH)`.
    * Calculates the distance in centimeters (`distanceCm`) and inches (`distanceInch`) based on the duration.
    * Sets the cursor to the top row (0, 0) of the LCD and prints "Distance:" followed by the distance in centimeters.
    * Sets the cursor to the second row (0, 1) of the LCD and prints "Distance:" followed by the distance in inches.
    * Introduces a small delay (`delay(10)`).

**dbuzzer (Python - `dbuzzer.py`):**

* Defines a `morse_code_dict` that maps uppercase letters, numbers, and space to their Morse code equivalents.
* Imports the `speech_recognition` library as `sr`.
* Creates a `Recognizer` object (`r`).
* Uses a `with sr.Microphone() as source:` block to access the microphone and record audio using `r.listen(source)`.
* Includes a `try...except` block to handle potential errors during speech recognition. It attempts to recognize the speech using `r.recognize_google(audio)` and prints the recognized text. If an error occurs, it prints an error message.
* Defines a `text_to_morse_code(text)` function:
    * Converts the input `text` to uppercase.
    * Iterates through each character in the text.
    * If the character is found in the `morse_code_dict`, its Morse code equivalent is appended to the `morse_code` list.
    * Otherwise, the character itself is appended (this handles characters not in the dictionary).
    * Finally, it joins the Morse code elements with spaces.
* Calls the `text_to_morse_code()` function with the recognized speech (`said`) to get the Morse code string.
* Prints the resulting Morse code.
* Imports the `Buzzer` class from `gpiozero` and the `sleep` function from `time`.
* Creates a `Buzzer` object connected to GPIO pin 17.
* Iterates through each character in the `morse_code_result`:
    * If the character is "-", it turns the buzzer on for a longer duration (1.25 seconds) and then off.
    * If the character is ".", it turns the buzzer on for a shorter duration (0.5 seconds) and then off.
    * If the character is " ", it introduces a longer pause (1.5 seconds) to represent a word space.
    * After each dot or dash, there's a short pause (0.5 seconds) to separate the elements of a letter.

## Why This Is "Silly and Basically Useless"

The core humor of this project lies in the intentional misapplication of assistive technologies. Providing visual distance information to someone who cannot see and auditory Morse code to someone who cannot hear creates a nonsensical and amusing outcome, perfectly fitting the "silly and basically useless" theme of the hackathon.
