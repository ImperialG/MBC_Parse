import xlrd
import os.path
import json
import sys
import wave
import contextlib

##
xlsPath = '035_01_00_Log.xls'
#hrRootPath = 'HeartAV_AudioFiles/'
audioFilesRootPath = 'HeartAV_AudioFiles/'
newDir ='config/'
hrpath = 'HeartAV_HeartRateFiles/HeartRate.xlsx'
logFileRootPath='MetaData/HeartAV_HCITaskLogfiles/'
audiopath = '/M1F1-uint8-AFsp.wav'

#checks if audio exists
if os.path.isfile(os.getcwd()+audiopath):
  #opens audio and gets duration
  with contextlib.closing(wave.open(os.getcwd()+audiopath,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = (int) (frames / float(rate))
    print("duration of file is:",duration)


#Xls file for heart rate data
hrworkbook = xlrd.open_workbook(os.getcwd()+"/"+hrpath, on_demand = True) #Takes some time to open
print("got past opening file")

currentLogFile = logFileRootPath + xlsPath
if os.path.isfile(currentLogFile):
    workbook = xlrd.open_workbook(currentLogFile, on_demand = True)
    worksheet = None
    jsonData = {}

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
        targetName = None
        audioRootName = None
        time = None
        hrSheetName = None

        #Assumes non empty row is well formatted
        if worksheet.cell(row, 0) != xlrd.empty_cell.value:
            targetName = str(worksheet.cell(row, 0).value)
            audioRootName = str(worksheet.cell(row, 1).value)
            time = str(worksheet.cell(row, 5).value)

        #Check if audio file exist
        audioFile =  audioFilesRootPath + audioRootName + '/' + 'vp_' + targetName +"_" + audioRootName + ".wav"
        if os.path.isfile(audioFile):
           print "audio file exist", audioFile

           try:
                if hrworkbook.sheet_by_name("vp_"  + targetName): #try to find Heartrate data
                    print "vp_" + targetName, " exists"
                    print json.dumps({'audioPath': audioFile, 'hrSheetName': hrSheetName },
                            sort_keys=True, indent=4, separators=(',', ': '))
           except:
                    print "vp_" + targetName, " !exists"

        else:
            #print "audio file does not  exist", audioFile
            pass
        """
        if hrworkbook.sheet_by_name("vp_"  + targetName): #try to find worksheet
              #Parse cols into json
              #store file path of wav
            print("vp_" + targetName + " exists")
        else:
            print("vp_" + targetName + " does not exist")"""
