import wave
import sys
import os

arg = sys.argv
if(len(arg) >= 2):
  filename = arg[1];
  origAudio = wave.open(filename,'r')
  frameRate = origAudio.getframerate()
  frames = origAudio.getnframes()
  nChannels = origAudio.getnchannels()
  sampWidth = origAudio.getsampwidth()
  duration = frames / frameRate
  
  origAudio.rewind()
  start = 0
  pos = origAudio.tell();
  while start < duration:
    origAudio.setpos(pos)
    end = min(start+59,duration)
    if(duration - (start + 59) < 30):
      end = duration
    
    framesToRead = (end - start) * frameRate;
    frame_data = origAudio.readframes(framesToRead);
    pos = origAudio.tell()
    newFile = filename + '_time=' + str(start/60)
    subchunk = wave.open(newFile,'w')
    subchunk.setnchannels(nChannels)
    subchunk.setsampwidth(sampWidth);
    subchunk.setframerate(frameRate)
    subchunk.writeframes(frame_data)
    subchunk.close()
    start = end + 1
  
  
  os.remove(filename);  

