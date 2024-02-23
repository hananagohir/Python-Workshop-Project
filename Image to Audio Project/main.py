
import pytesseract # allows Python to interact with Tesseract OCR (Optical Character Recognition engine)
from PIL import Image # imports the Image class from Pillow for image processing 
from gtts import gTTS # Google text-to-speech is used to convert text to audio
import pygame # pygame used to load and play audio

# tesseract_cmd needs to be shown the path to tesseract.exe for pytesseract to work correctly
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\14379\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


# function image_to_text_to_audio takes two parameters image_path and output_audio_path
def image_to_text_to_audio(image_path, output_audio_path):

    image = Image.open(image_path) # Image class from Pillow processess the image

    text = pytesseract.image_to_string(image) # the image inconverted from image to a string of text

    print("This is the extracted image text: ", text)  # for debugging reasons
    
    tts = gTTS(text=text, lang ='en') # converts the text to audio in the english language

    tts.save(output_audio_path) # saves the converted audio in output_audio_path

    pygame.mixer.init() # initializes pygame mixer

    pygame.mixer.music.load(output_audio_path) # loads audio into pygame mixer for playback

    pygame.mixer.music.play() # plays the audio file

    # while loop is needed to make sure the playback finishes before being exited
    while pygame.mixer.music.get_busy(): # returns true if the audio is still playing
        pygame.time.Clock().tick(10) # waits 1/10th of a second before checking if audio is still playing



image_path = r'C:\Users\14379\Desktop\Image to Audio Project\images.png' # path for original image file
output_audio_path = r'C:\Users\14379\Desktop\Image to Audio Project\audio_output.mp3' # path for output file
image_to_text_to_audio(image_path, output_audio_path) # calling function

