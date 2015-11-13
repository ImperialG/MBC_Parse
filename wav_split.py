import wave
import sys
import os


def traverseThroughFolder(current_path):
  files_and_folders = os.listdir(current_path);
  for file in files_and_folders:  
    file_path = current_path + '/' + file;
    if(os.path.isdir(file_path)):
      traverseThroughFolder(file_path,time_csv,hr_csv_dir)
    else:
      splitAudio(file_path); #splits audio file into subchunks and deletes the original file
  return

def splitAudio(file_path):
  int window_length = 59; #duration of subchunks in seconds
  origAudio = wave.open(file_path,'r')
  try:
    frameRate = origAudio.getframerate()
    frames = origAudio.getnframes()
    nChannels = origAudio.getnchannels()
    sampWidth = origAudio.getsampwidth()
    duration = frames / frameRate 
  
    start = 0
    pos = origAudio.tell()
    while start < duration:
      origAudio.setpos(pos)
      end = min(start+window_length,duration)
      if(duration - (start + window_length) <= window_length/2):
        end = duration
    
      framesToRead = (end - start) * frameRate
      frame_data = origAudio.readframes(framesToRead)
      pos = origAudio.tell()
      newFile = filename + '_time=' + str(start)
      subchunk = wave.open(newFile,'w')
      try:
        subchunk.setnchannels(nChannels)
        subchunk.setsampwidth(sampWidth)
        subchunk.setframerate(frameRate)
        subchunk.writeframes(frame_data)
      finally:
        subchunk.close()
    finally:
      origAudio.close()
    start = end + 1
  
  
  os.remove(filename);  
  

arg = sys.argv
if(len(arg) >= 2):
  root_dir = arg[1];
  if(os.path.isdir(root_dir):
    traverseThroughFolder(root_dir
  

