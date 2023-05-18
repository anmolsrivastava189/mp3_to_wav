from os import path
from pydub import AudioSegment

input_file = "input.mp3"    # write the name of your mp3 file here
output_file = "output.wav"    # write the name you want to convert the mp3 file
  
# Conversion takes place here
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")