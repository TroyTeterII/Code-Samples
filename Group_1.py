import csv, datetime        
##event = 'Dense Fog'

def storm_by_event(event):

    indiana_storms = csv.DictReader(open('Indiana_Storms.csv','r'))

    for entry in indiana_storms:
        if entry['EVENT_TYPE'] == event:
            date_full = entry['BEGIN_DATE_TIME'].split(' ')
            date = date_full[0]
##            print('A',entry['EVENT_TYPE'],'happened on',date+' '*(10-len(date))+'in',\
##                  entry['CZ_NAME'],'county')
            print('\nOn',date,entry['EPISODE_NARRATIVE'],'This was reported in',\
                  entry['CZ_NAME'],'county.',entry['EVENT_NARRATIVE'],'\n')




##date = '5/15/2015'

def storm_by_date(date):

    indiana_storms = csv.DictReader(open('Indiana_Storms.csv','r'))

    for entry in indiana_storms:
        date_full = entry['BEGIN_DATE_TIME'].split(' ')
        date1 = date_full[0]
        if date1 == date:
##            print('A',entry['EVENT_TYPE'],'happened on',date1,'in',\
##                  entry['CZ_NAME'],'county')
            print('\nOn',ddate.strftime('%A the %d of %B'),entry['EPISODE_NARRATIVE'],'This was reported in',\
                  entry['CZ_NAME'],'county.',entry['EVENT_NARRATIVE'],'\n')




while True:
    intput = input('Would you like to search by date or by event or type "stop" to close? ').lower()

    if intput == 'event':
        event = input('Please enter the type of weather you are searching for: ').title()
        storm_by_event(event)

    elif intput == 'date':
        date = input('Please enter the date you are searching for in YYYY/MM/DD format: ')
        date_list = date.split('/')
        month_0 = date_list[1].replace('0', '')
        day_0 = date_list[2].replace('0', '')
        new_date = month_0+'/'+day_0+'/'+date_list[0]
        ddate = datetime.date(int(date_list[0]), int(month_0), int(day_0))

        storm_by_date(new_date)
    elif intput == 'stop':
        break
    
    else:
        print('That is not a valid selection. Please try again.')