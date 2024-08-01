'''
Written by Alec Olson
Last edited 08/01/2024

Script to pull yearly weather data for St. Paul, MN and save the data to a table in an html file

Class:
- GSOY
    - GSOY stands for Global Summary of the Year
    - Each instance of this class represents a year's worth of data.
    - Each object has two attributes:
        - self.year (an integer)
        - self.attributes (a list containing all the data for that year)
    - Each object has two getters, one to return self.year and one to return self.attributes

Function:
- getGSOY(years)
    - This function takes one parameter, years, which is a list of years
    - This function then requests a summary of yearly weather data from the NOAA for St. Paul, MN for each of these years
    - Each year's data is stored in a GSOY object
    - Each GSOY object is then added to a list, titled gsoyList
    - This data is then combined into a csv file, with one row for each year
    - This csv file is then transformed into an html file so that it can easily be displayed in web browser
    - Return value: the name of the html file which contains the table of weather data
'''


import requests
import pandas as pd

class GSOY:
    def __init__(self, year, list):
        self.year = year
        self.attributes = list

    def getYear(self):
        return self.year

    def getAttributes(self):
        return self.attributes


def getGSOY(years):     # years is a list of years
    gsoyList = []
    intermediateURL = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USC00218450&'
    for i in range(len(years)):
        year = years[i]
        response = requests.get(f'{intermediateURL}startdate={year}-01-01&enddate={year}-12-31', headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})
        if response.status_code == 200:
            print(response.status_code)
            gsoy = response.json()
            if gsoy != {}:
                n = len(gsoy['results'])
                attributeList = [0] * n
                for j in range(n):
                    dict = gsoy['results'][j]
                    combine = [dict['datatype'], dict['value']]
                    attributeList[j] = combine
                gsoyList.append(GSOY(year, attributeList))

    with open('gsoyfile.csv', 'w') as fp:
        fp.write('YEAR, ')
        for i in range(len(gsoyList[0].getAttributes())-1):
            fp.write(f'{gsoyList[0].getAttributes()[i][0]}, ')
        fp.write(f'{gsoyList[0].getAttributes()[-1][0]}')
        fp.write('\n')
        for i in range(len(gsoyList)):
            fp.write(f'{gsoyList[i].getYear()}, ')
            for j in range(len(gsoyList[i].getAttributes())-1):
                fp.write(f'{gsoyList[i].getAttributes()[j][1]}, ')
            fp.write(f'{gsoyList[i].getAttributes()[-1][1]}')
            fp.write('\n')
    
    a = pd.read_csv('gsoyfile.csv')
    a.to_html('table.html')
    #html_file = a.to_html()

    return 'table.html'


#baseURL = 'https://www.ncei.noaa.gov/cdo-web/api/v2/'

#response = requests.get(f"{baseURL}/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01", headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})
# response = requests.get(f"{baseURL}/datasets/GSOM", headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})
# print(response.status_code)
# datasets = response.json()
# for key in datasets["results"]:
#    print(key["name"])
# print(datasets)

#response = requests.get(f"{baseURL}/data?datasetid=GSOM&stationid=GHCND:USC00010008&units=standard&startdate=2010-05-01&enddate=2010-05-31", headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})
# response = requests.get(f"{baseURL}/data?datasetid=GSOM&stationid=GHCND:USC00218450&startdate=2010-05-01&enddate=2010-05-31", headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})    #US1MNHN0025 is at Target Field
# print(response.status_code)
# gsom = response.json()
# for dict in gsom["results"]:
#     print(f'{dict["datatype"]}: {dict["value"]}')
#print(gsom)

#gsoyList = []

#intermediateURL = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USC00218450&'
# response = requests.get(f"{intermediateURL}startdate=2011-01-01&enddate=2011-12-31", headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})
# print(response.status_code)
# gsoy = response.json()
# print(gsoy)

# years = list(range(2001, 2021))

#for i in range(20):
#    year = years[i]
#    print(year)
#    response = requests.get(f"{intermediateURL}startdate={year}-01-01&enddate={year}-12-31", headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})
#    print(response.status_code)
#    if response.status_code == 200:
#        gsoy = response.json()
#        if gsoy != {}:
#            #print(gsoy)
#            n = len(gsoy["results"])
#            attributeList = [0] * n
#            for j in range(n):
#                dict = gsoy["results"][j]
#                combine = [dict["datatype"], dict["value"]]
#                attributeList[j] = combine
#            gsoyList.append(GSOY(year, attributeList))


# for i in range(len(gsoyList)):
#     print(gsoyList[i].getYear())
#     print(gsoyList[i].getAttributes())

# with open('gsoyfile2.csv', 'w') as fp:
#     fp.write('YEAR, ')
#     for i in range(len(gsoyList[0].getAttributes())-1):
#         fp.write(f'{gsoyList[0].getAttributes()[i][0]}, ')
#     fp.write(f'{gsoyList[0].getAttributes()[-1][0]}')
#     fp.write('\n')
#     for i in range(len(gsoyList)):
#         fp.write(f'{gsoyList[i].getYear()}, ')
#         for j in range(len(gsoyList[i].getAttributes())-1):
#             fp.write(f'{gsoyList[i].getAttributes()[j][1]}, ')
#         fp.write(f'{gsoyList[i].getAttributes()[-1][1]}')
#         fp.write('\n')

# response = requests.get(f"{baseURL}/data?datasetid=GSOY&stationid=GHCND:USC00218450&startdate=2010-01-01&enddate=2010-12-31", headers={'token': 'AySiHZbDlhnVHVVZsdimIoQAyhrxIuEx'})    #US1MNHN0025 is at Target Field
# print(response.status_code)
# gsoy = response.json()
# #print(gsoy["results"])
# for dict in gsoy["results"]:
#     print(f'{dict["datatype"]}: {dict["value"]}')