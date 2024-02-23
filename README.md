# Project Overview

The goal of this project is to convert any image to text, and then convert the extracted text to speech using python. 

The python script will acheive the following:
* Open the image
* Convert the image to string of text
* Convert text to speech
* Play the audio 


# Project GamePlan

* Import Nesessary Packages
    * `pytesseract`
        * link the correct path to the `pytesseract` program
  * `Pillow (PIL)` import `Image` class
  * `Google text-to-speech (gtts)` import `gTTS` class
  * import `pygame`

* Open image
  * Use `pillow (PIL)` and open the image

* Convert text to speech
  * use `Google text-to-speech (gtts)` to convert the extracted text to audio
  * save the speech to a file

* Play the audio file
  * use `pygame` to load and play the audio file


# How To Run The project
1.  Clone this repository to your local machine: `git clone https://github.com/HananaG/Python-Workshop-Project`

2.  Change into the project directory: `cd Python-Workshop-Project`

3.  Install the required dependencies: `pip install pytesseract Pillow gTTS pygame`

4.  Once the installation is complete, you can start the project: `python main.py`


# Resources

* Pre-Workshop Setup Guide: Pre-Workshop Environment Setup.pdf

* Presenation slides: https://python-workshop-hananag.my.canva.site/
