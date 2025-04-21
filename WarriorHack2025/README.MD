# 🤪 The Utterly Impractical Sensory Swap Device 🤪

**Our Hilariously Useless Hackathon Creation!**

For this hackathon, we took on the *important* task of building something wonderfully, spectacularly **impractical**. Behold our masterpiece: a device featuring the "Blind Visor" (bvisor) and the "Deaf Buzzer" (dbuzzer), designed with a comical and utterly useless swap of intended functionality. Prepare for peak sensory confusion!

## 🎯 Our Gloriously Pointless Goal 🎯

We aimed to create a device where the visually impaired could "see" distance on a screen, and the hearing impaired could "hear" spoken words as beeping Morse code. The result? The bvisor and dbuzzer working in perfect, hilarious opposition to their typical uses. Mission accomplished!

## ⚙️ The "Useless" Components & How They (Don't Really) Help ⚙️

### 👓 The "Blind Visor" (bvisor - Arduino) 👓

Imagine a blind person trying to read a screen... that's the spirit!

* **🧠 Arduino:** The tiny brain making all the (wrong) decisions.
* **📏 Ultrasonic Distance Sensor:** Like a bat, it sends out sound to measure how far things are.
    * **How it (uselessly) works:** It beeps, waits for the echo, and tells the Arduino the distance.
* **🎛️ Potentiometer:** (Probably just chilling, maybe for future *even more useless* features).
* **📺 LCD Display (16x2):** Shows numbers and letters.
    * **How it (uselessly) works:** It proudly displays the distance in centimeters and inches for someone who can't see it.
* **🔋 9V Battery:** Powering this beacon of visual information for the blind.

    **Libraries You'll Need (Arduino):**

    ```
    LiquidCrystal.h  // For talking to the LCD screen
    ```

### 👂 The "Deaf Buzzer" (dbuzzer - Raspberry Pi) 👂

Now picture trying to understand beeps when you can't hear... genius!

* **<0xF0><0x9F><0xA7><0x8E> Raspberry Pi:** The mini-computer orchestrating the silent symphony.
* **🔋 PiSugar:** Keeping our beeping dream portable.
* **📢 Buzzer:** Makes the "sounds" of Morse code.
    * **How it (uselessly) works:** It beeps short for dots (`.`) and long for dashes (`-`).
* **🎤 Microphone:** Listens to the world.
    * **How it (uselessly) works:** It picks up spoken words, ready to be turned into inaudible beeps.
* **🗣️ `speech_recognition` Library:** Turns spoken words into text.
    * **How it (uselessly) works:** It tries its best to understand speech so it can beep it out.
* **🕹️ `gpiozero` Library:** Controls the buzzer.
    * **How it (uselessly) works:** It tells the buzzer when and for how long to beep.

    **Libraries You'll Need (Python):**

    ```bash
    pip install SpeechRecognition
    pip install gpiozero
    ```

## 📜 The "Useless" Code in Action 📜

### 🤖 bvisor (Arduino - `naked_bvisor.ino`) 🤖

```arduino
#include <LiquidCrystal.h>
LiquidCrystal lcd(1, 2, 4, 5, 6, 7);
const int trigPin = 9;
const int echoPin = 10;
long duration;
int distanceCm, distanceInch;
void setup() {
  lcd.begin(16, 2);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * 0.034 / 2;
  distanceInch = duration * 0.0133 / 2;
  lcd.setCursor(0, 0);
  lcd.print("Distance: ");
  lcd.print(distanceCm);
  lcd.print(" cm");
  delay(10);
  lcd.setCursor(0, 1);
  lcd.print("Distance: ");
  lcd.print(distanceInch);
  lcd.print(" inch");
  delay(10);
}
