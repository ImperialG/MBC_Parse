import os
import sys
import re
import csv
import datetime
import string
import xlrd

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
  user_meta_file = meta_dir + '/' + cand + '_Log.xls';
  if os.path.isfile(user_meta_file):
    workbook = xlrd.open_workbook(user_meta_file, on_demand = True)
    try:
      worksheet = workbook.sheet_by_name("Tabelle1")
      time = None
      remove = string.whitespace;
      for row in range(worksheet.nrows):
        if(str(worksheet.cell(row, 1).value).lower().translate(None,remove) == task.lower().translate(None,remove)):
          time = worksheet.cell(row, 5).value
          name = cand+'_'+task;
          outfile.write(name+','+str(time)+'\n');
          break;
      if(time == None):
        print('filepath',user_meta_file);
        print('not found time for',task);
    except:
      print("Sheet doesn't exist in file", user_meta_file);
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

