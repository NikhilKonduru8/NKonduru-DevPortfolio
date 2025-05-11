# Video Emotion Analysis Script

This script analyzes the emotions expressed by faces detected in a video file. It utilizes the `fer` library for facial emotion recognition and the `moviepy` library for video handling.

**Note:** This script represents one part of an AI therapist application developed for a high school hackathon. It focuses on analyzing the emotional state of an individual from video input.

## Functionality

The script performs the following steps:

1.  **Loads a video file:** It takes a video file named `aditya.mov` as input.
2.  **Detects faces and analyzes emotions:** Using the `fer` library with MTCNN for face detection, it analyzes each frame of the video to identify faces and predict the intensity of seven basic emotions: angry, disgust, fear, happy, sad, surprise, and neutral.
3.  **Optionally displays live analysis:** If enabled, the script can show a live video feed with bounding boxes around detected faces and their corresponding emotion predictions.
4.  **Converts analysis to a DataFrame:** The raw analysis data is converted into a pandas DataFrame for easier manipulation.
5.  **Calculates total emotion scores:** It sums the scores for each emotion across all analyzed frames.
6.  **Determines the main emotion:** It identifies the emotion with the highest total score throughout the entire video.
7.  **Prints the main emotion:** Finally, it prints the identified main emotion to the console.

## Libraries Used

* `fer`: For facial emotion recognition.
* `moviepy`: For handling video files.
* `pandas`: For data manipulation (specifically converting analysis data into a DataFrame).

## Input

The script expects a video file named `aditya.mov` to be present in the same directory where the script is executed.

## Output

The script prints a single line to the console indicating the main emotion detected throughout the video. For example:
