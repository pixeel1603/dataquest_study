import csv
import datetime

#Prepare data
data=[]
file = open('guns.csv')
prepared_data = csv.reader(file)
data = list(prepared_data)
headers = data[0]
data = data[1:len(data)]

#Actual Lists
dates = []
sex = []
race = []

#Import data to lists
for row in data:
    year = int(row[1])
    month = int(row[2])
    dates.append(datetime.datetime(year=year, month=month,day=1))
    sex.append(row[5])
    race.append(row[7])
year_counts = {}
date_counts = {}
sex_counts = {}
race_counts = {}
for d in dates:
    if d in date_counts:
        date_counts[d]+=1
    else:
        date_counts[d]=1
for s in sex:
    if s in sex_counts:
        sex_counts[s]+=1
    else:
        sex_counts[s]=1
for r in race:
    if r in race_counts:
        race_counts[r]+=1
    else:
        race_counts[r]=1
#Base counts: date_counts - count of accidents by dates; sex_counts-by sex; race_counts - by race
#Result:        
#Most accidets has been made by white males it isn't depends on year or month


#Now let's find percentage
#Prepare data
census=[]
file = open('census.csv')
prepared_census = csv.reader(file)
census = list(prepared_census)
#print(census)

#Step 7. Find all accidents by races (percentage)
mapping = {}
cen_row = census[1]
mapping['Asian/Pacific Islander'] = int(cen_row[14])+int(cen_row[15])
mapping['Black'] = int(cen_row[12])
mapping['Hispanic'] = int(cen_row[11])
mapping['Native American/Native Alaskan'] = int(cen_row[13])
mapping['White'] = int(cen_row[10])
race_per_hundredk = {}
for key,value in race_counts.items():
    race_per_hundredk[key]= (value/mapping[key])*100000
#print(race_per_hundredk)

#Step8. Find Homicide accidents by races (percentage)
race = []
intends= []
for row in data:
    race.append(row[7])
    intents.append(row[3])
homicide_race_counts = {}
for i,r in enumerate(race):
    if intents[i] == 'Homicide':
        if r in homicide_race_counts:
            homicide_race_counts[r]+=1
        else:
            homicide_race_counts[r]=1
homicide_race_counts_hundreds={}
for key,value in homicide_race_counts.items():
    homicide_race_counts_hundreds[key]= (value/mapping[key])*100000
print(homicide_race_counts)
print(homicide_race_counts_hundreds)
