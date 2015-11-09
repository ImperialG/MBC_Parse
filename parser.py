import xlrd
import os.path
import json
import sys

##
xlsPath = '035_01_00_Log.xls'
hrRootPath = 'HeartAV_AudioFiles/'
newDir ='config/'
hrpath = 'HeartAV_HeartRateFiles/HeartRate.xlsx'
logFileRootPath='MetaData/HeartAV_HCITaskLogfiles/'
#For each log file
#Indexed by row, col of worksheet

data = {}

#Xls file for heart rate data
hrworkbook = xlrd.open_workbook(os.getcwd()+"/"+hrpath, on_demand = True) #Takes some time to open


currentLogFile = logFileRootPath + xlsPath
if os.path.isfile(currentLogFile):
    workbook = xlrd.open_workbook(currentLogFile, on_demand = True)
    worksheet = None
    try:
        worksheet = workbook.sheet_by_name("Tabelle1") #We assume the log data is always on this sheet
    except:
        print("Sheet doesn't exist in file", xlsPath)
    else:
        #TODO: Uncomment when in for loop
        #continue #Skip and parse the next log file
        pass

    #sys.exit(0)

    #Parse every non empty row in worksheet
    for row in range(worksheet.nrows):
        print("row loop")


        #Assumes non empty row is well formatted
        if worksheet.cell(row, 0) != xlrd.empty_cell.value:
            targetName = worksheet(row, 0)
            name = worksheet.cell(row, 1)
            time = workbook.cell(row, 5)
            print targetName, name, time
      #if os.path.isfile(hrRootPath+'/' + name + '/' + targetName ".wav"):
        if hrworkbook.sheet_by_name("vp_"  + targetName): #try to find worksheet
              #Parse cols into json
              #store file path of wav
            print("vp_" + targetName + " exists")
        else:
            print("vp_" + targetName + " does not exist")
