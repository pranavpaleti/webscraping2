from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(START_URL)
soup=bs(page.text,'html.parser')
starsTable=soup.find_all('table')

tempList=[]
tableRows=starsTable[7].find_all('tr')

for tr in tableRows:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    tempList.append(row)

starName=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(tempList)):
    starName.append(tempList[i][1])
    distance.append(tempList[i][2])
    mass.append(tempList[i][3])
    radius.append(tempList[i][4])

csvFile=pd.DataFrame(list(zip(starName,distance,mass,radius)),columns=['star name','distance','mass','radius'])
csvFile.to_csv('BrightStars2.csv')