#Specify root directory

#Read Log file
#For each log file
#For each correct formatted row (A, B, C, D, E, F, G) = (_, activity, _, _, date, time, _ )
print("before import")

import xlrd
import os.path
import json


##
xlsPath = '035_01_00_Log.xls'
hrRootPath = 'HeartAV_AudioFiles/'
newDir ='config/'
hrpath = 'HeartRate.xlsx'
#For each log file
#Indexed by row, col of worksheet

data = {}


if os.path.isfile(os.getcwd()+"/"+xlsPath):
  workbook = xlrd.open_workbook(os.getcwd()+"/"+xlsPath, on_demand = True)
  try:
    sheet = workbook.sheet_by_name("Tabelle1") #gets worksheet by name
  except: 
    print("false") #if sheet does not exist
  else:
      print(sheet) #sheet exists
  print("get here")
  hrworkbook = xlrd.open_workbook(os.getcwd()+"/"+hrpath) #open heart rate workbook this seems to fail though
  worksheet = workbook.sheet_by_index(0)
  for row in range(worksheet.nrows):
    print("row loop")
    #Assumes non empty row is well formatted
    if worksheet.cell(row, 0) != xlrd.empty_cell.value:
      targetName = worksheet(row, 0)
      name = worksheet.cell(row, 1)
      time = workbook.cell(row, 5)
      #if os.path.isfile(hrRootPath+'/' + name + '/' + targetName ".wav"):
      if hrworkbook.sheet_by_name("vp_"  + targetName): #try to find worksheet
        #Parse cols into json
        #store file path of wav
        print("vp_" + targetName + " exists")
      else:
        print("vp_" + targetName + " does not exist")
                                                                                                                                                                                 #data[""]



