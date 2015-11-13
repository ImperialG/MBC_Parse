import os
import sys
import re
import csv
import datetime
import string

def traverseThroughFolder(current_path,time_csv,hr_csv_dir):
  files_and_folders = os.listdir(current_path);
  for file in files_and_folders:    
    file_path = current_path + '/' + file;
    if(os.path.isdir(file_path)):
      traverseThroughFolder(file_path,time_csv,hr_csv_dir)
    else:
      pattern = r'vp_(\d+_\d+_\d+)_(\w+)_time=(\d+).wav'
      pat = re.search(pattern,file);
      if(pat):
        pat = pat.groups();
        cand = pat[0];
        task = pat[1];
        time = pat[2];
        print(cand)
        print(task);
        print(time);
        appendHRtoFileName(file_path,cand,task,time_csv,hr_csv_dir)
  return

def appendHRtoFileName(file_path,cand,task,time_csv,hr_csv_dir):
  hr_file_path = hr_csv_dir + '/HeartRate.vp_' + cand + '.csv';
  if os.path.isfile(hr_file_path):
    hr_file = open(hr_file_path,'rt')
    try:
      time = find(time_csv,0,1,cand+'_'+task,',');
      if(time != None):
        hr = find(hr_file,0,2,time,';');
        if(hr != None):
          print(time,hr)
        else:
          print('hr does not exists',time);                  
      else:
        print('time does not exists',cand+'_'+task);
      #find heart rate at that time
      #then rename original file by appending heart rate
    finally:
       hr_file.close();
  else:
    print('hr file does not exist',hr_file_path);  
  return  

def find(csv_file,source_col,target_col,search_key,delimt):
  reader = csv.reader(csv_file, delimiter=delimt)
  for row in reader:
    if(row[source_col] == search_key):
      return row[target_col];
  return None

argv = sys.argv
if(len(argv) >= 4):
  current_path = argv[1]; #folder in which all wave files are
  csv_path = argv[2]; #csv file with file name and start time for all candidates and tasks
  heart_rate = argv[3]; #path to heart rate csv files
  
  csv_file = open(csv_path,'rt')
  try:
    traverseThroughFolder(current_path,csv_file,heart_rate)
  finally:
    csv_file.close()

