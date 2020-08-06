import requests
import zipfile
import pandas as pd
import os
import sys

url = "https://www1.nseindia.com/content/historical/EQUITIES/2020/AUG/cm05AUG2020bhav.csv.zip"


def GetData():
    reqData = requests.get(url, allow_redirects = True)
    open('download.zip', 'wb').write(reqData.content)

    zipData = zipfile.ZipFile("download.zip")
    Namelist = zipData.namelist()
    CsvFileName = Namelist[0]
    DataFrame = pd.read_csv(zipData.open(CsvFileName))
    return DataFrame

def CheckMyStocks(DataFrame, MyList):
    retString = ""
    for i in MyList:
        idx = DataFrame.loc[DataFrame.SYMBOL == i].index
        retString = retString + str(DataFrame.loc[idx[0]])
        retString = retString + "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

    return retString
        

Report = ""
DataFrame = GetData()
DataFrame["MAX_DAILY_GAIN"] = DataFrame["CLOSE"] - DataFrame["OPEN"]
DataFrame["GAIN_PERCENTAGE"] = (DataFrame["MAX_DAILY_GAIN"] / DataFrame["OPEN"]) * 100
DataFrame.sort_values(by = "GAIN_PERCENTAGE", ascending = False, na_position='first', inplace = True)
Report = Report + "Hi User, bringing you Todays market Analysis \nTop Ten stocks by % gain  are :\n "
STR = DataFrame.head(10)
Report = Report + str(STR)
Report = Report + "\n\n========================================================\n\nOn the other hand the 10 worst performing stocks by % gain are\n"
STR = DataFrame.tail(10)
Report = Report + str(STR)

Report = Report + "\n******************************************************************************\n\nTop 10 stocks by profit gained are as follows:\n"
DataFrame.sort_values(by = "MAX_DAILY_GAIN", ascending = False, na_position='first', inplace = True)
STR = DataFrame.head(10)
Report = Report + str(STR)

Report = Report + "\n\n========================================================\n\nOn the other hand the 10 worst performing stocks by profit earned  are\n"
STR = DataFrame.tail(10)
Report = Report + str(STR)
Report = Report + "\n\n*****************************************************************************\n\n"
Report = Report + "\n\n========================================================\n\n 50 most traded share quatitywise are as follows \n\n"
DataFrame.sort_values(by = "TOTTRDQTY", ascending = False, na_position='first', inplace = True)
STR = DataFrame.head(50)
Report = Report + str(STR)
Report = Report + "\n\n*****************************************************************************\n\n"
Report = Report + "The Analysis of your choosen shares is as follows:\n"
MyList = ["RELIANCE", "INDOCO", "PPL", "WIPRO", "TCS"]
STR = CheckMyStocks(DataFrame, MyList)
Report = Report + STR




print (Report)

os.remove("download.zip")
    
