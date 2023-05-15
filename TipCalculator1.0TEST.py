from __future__ import division
from decimal import Decimal
print('Welcome to the Tip Calculator!! Before I begin I will need some information.'
      )

#CURRENCY PRINT FORMATTING
#ONLY WORKS WITH FLOATS
#amount = 123456.78
#currency = "${:,.2f}".format(amount)
#print(currency)



TfundsASK = input('What is the total amount of tip funds in dollars and cents: ')
#total tips
Tfunds = float(TfundsASK)
print('Amount Entered: '+"${:,.2f}".format(Tfunds))


ThoursASK = input('What is the total amount of hours worked? :')
#hours worked
Thours = float(ThoursASK)
print('Hours Entered: '+str(Thours))

#tips per hour as a rounded decimal
AvgTip = Decimal(str(Tfunds)) / Decimal(str(Thours))
RoundTip = round(AvgTip, 2)
print('Here are the Average funds divided by the average hours:')
print(RoundTip)

#create a list of people hours in decimal form
print('Okay, now input each persons hours in order.')
Hourslist = []
while True:
    entry = input('Enter new amount or press "q" to quit: ')
    if entry == 'q':
        break
    try:
        Hourslist.append(float(entry))
    except:
        print("Not a valid number")

print('Here is the list of hours:')
print(Hourslist)
Tiplist = []        
#multiply person's hours by AvgTip
for i in Hourslist:
    Newtip = Decimal(i) * RoundTip
    
    Newroundtip = round(Newtip, 2)
    
    Tiplist.append(str(Newroundtip))

print('Here is the list of each persons tips in order:')    
print(Tiplist)


    

