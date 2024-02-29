import pandas as pd
import glob
import csv

#Define file names
CityIdSheet = '/Users/aaryangupta/Desktop/CSVFiles/CityIDToName.csv'
FriscoFile = '/Users/aaryangupta/Desktop/CSVFiles/CityMasterFiles/FriscoMasterFile.csv'
PlanoFile = '/Users/aaryangupta/Desktop/CSVFiles/CityMasterFiles/PlanoMasterFile.csv'
DallasFile = '/Users/aaryangupta/Desktop/CSVFiles/CityMasterFiles/DallasMasterFile.csv'
CityIdSheetReader = csv.reader(open(CityIdSheet))

#Get all uploaded files
location = '/Users/aaryangupta/Desktop/CSVFiles/UploadedFiles/*.csv'  # name of folder on your device
csv_files = glob.glob(location)

#Combine sheets
for csv_file in csv_files:

    print("\n")

    #Create CityIdSheet reader
    CityIdSheetReader = csv.reader(open(CityIdSheet))

    #Open file and read lines
    csv_fileOpened = open(csv_file)
    data = pd.read_csv(csv_file)

    #Get City ID
    lastColumn = data.columns[2]
    cityID = ""
    for i in lastColumn:
        if i.isdigit():
            cityID = cityID + i

    #Find which city
    currentCity = ""
    for row in CityIdSheetReader:
        if row[0] == cityID:
            currentCity = row[1]
            break
    print(currentCity)

    #Combine tables
    csvFileDataTable = pd.read_csv(csv_file)

    if currentCity == "Plano":
        PlanoDataTable = pd.read_csv(PlanoFile)
        PlanoNewFile = pd.merge(csvFileDataTable, PlanoDataTable, how='outer')
        del PlanoNewFile[lastColumn]
        print(PlanoNewFile)

    elif currentCity == "Frisco":
        FriscoDataTable = pd.read_csv(FriscoFile)
        FriscoNewFile = pd.merge(csvFileDataTable, FriscoDataTable, how='outer')
        del FriscoNewFile[lastColumn]
        print(FriscoNewFile)

    else :
        DallasDataTable = pd.read_csv(DallasFile)
        DallasNewFile = pd.merge(csvFileDataTable, DallasDataTable, how='outer')
        del DallasNewFile[lastColumn]
        print(DallasNewFile)


#Convert dataframe to CSV
print("\n")
finalFile = pd.concat([PlanoNewFile, FriscoNewFile, DallasNewFile])
finalFile.sort_values('HouseID', ascending=True, inplace=True)
print(finalFile)
finalFile.to_csv("/Users/aaryangupta/Desktop/CSVFiles/AllData/alldata.csv", index=False) #name of new folder
