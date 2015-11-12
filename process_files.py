import os
import sys
import re
import csv

def traverseThroughFolder(current_path,out_path,meta_dir):
  files_and_folders = os.listdir(current_path);
  for file in files_and_folders:    
    file_path = current_path + '/' + file;
    if(os.path.isdir(file_path)):
      traverseThroughFolder(file_path,out_path,meta_dir)
    else:
      pattern = r'vp_(\d+_\d+_\d+)_(\w+).wav'
      pat = re.search(pattern,file);
      if(pat):
        pat = pat.groups();
        cand = pat[0];
        task = pat[1];
        appendToCSV(file_path,cand,task,meta_dir,out_path);
  return

def appendToCSV(file_path,cand,task,meta_dir,outfile):
  user_meta_file = meta_dir + '/' + cand;
  #open tabelle1
  #find row with column 2 = task and get time
  time = 0;
  outfile.write(str(file_path)+','+str(time)+'\n');
  #append file_path and time to end of outfile
  return  

argv = sys.argv
if(len(argv) >= 4):
  current_path = argv[1];
  meta_dir = argv[2];
  out_path = argv[3];
  out_file = open(out_path,'a+')
  try:
    traverseThroughFolder(current_path,out_file,meta_dir)
  finally:
    out_file.close()

