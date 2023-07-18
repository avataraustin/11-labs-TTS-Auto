import requests
import os
import time



# Requires text file to be processed be named "source.txt"
# and the file will chunk by word lines separated by an 
# empty line space in the txt file.

#process source.txt file and chunk by blank lines
with open('source.txt') as f:
    textchunks = f.read().split('\n\n')
#create a stored list of the text chunks for TTS use later
textchunks = [chunk.strip() for chunk in textchunks]




ElevenLab_API = os.environ['11L-API'] #secret api key

# My voices:
# Tiberius voice: TBcAA87Dw9PhPyARtmMq
# GRUFF American voice: s4cuAbUrEz6av0dOGY2i
# Thomas voice: iGwp309gJqQYefiiosaf
Tiberius = "TBcAA87Dw9PhPyARtmMq"
Gruff = "s4cuAbUrEz6av0dOGY2i"
Thomas = "iGwp309gJqQYefiiosaf"

url = "https://api.elevenlabs.io/v1/text-to-speech/"+Tiberius

CHUNK_SIZE = 1024

for i in range(len(textchunks)):

  headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": ElevenLab_API
  }
  
  data = {
    "text": textchunks[i],
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.35,
      "similarity_boost": 0.65
    }
  }
  
  response = requests.post(url, json=data, headers=headers)
  
  with open('output-'+str(i)+'.mp3', 'wb') as f:
      for ttschunk in response.iter_content(chunk_size=CHUNK_SIZE):
          if ttschunk:
              f.write(ttschunk)
  time.sleep(10)  #time to sleep in seconds between mp3 file generations