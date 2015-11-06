#Specify root directory

#Read Log file
#For each log file
#For each correct formatted row (A, B, C, D, E, F, G) = (_, activity, _, _, date, time, _ )

import xlrd
import os.path
import json

##
xlsPath = 'MetaData/HeartAV_HCITaskLogfiles/035_01_00_Log.xls'
hrRootPath = 'HeartAV_AudioFiles/'
newDir ='config/'
hrWorkSheet = 'HeartAV_HeartRateFiles/HeartRate.xlsx'

#For each log file
#Indexed by row, col of worksheet

data = {}


if os.path.isfile(xlsPath):
        workbook = xlrd.open_workbook(xlsPath, on_demand = True)
        worksheet = workbook.sheet_by_index(0)
        for row in range(worksheet.nrows):
        #Assumes non empty row is well formatted
            if worksheet.cell(row, 0) != xlrd.empty_cell.value:
                targetName = worksheet(row, 0)
                name = worksheet.cell(row, 1)
                time = workbook.cell(row, 5)
                                                                                        if os.path.isfile(hrRootPath+'/' + name + '/' + targetName ".wav"):
                                                                                            if "vp_"  + targetName #try to find worksheet
                                                                                            #Parse cols into json
                                                                                                                                                                 #store file path of wav

                                                                                                                                                                                 data[""]



