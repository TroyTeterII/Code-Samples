
#function to pull data from cvs file
def listCharacters():
    people =csv.DictReader(open("starwars.csv","r"))
    for entry in people:
        print(entry)
    
#print out character name, actor name, and birthdate

#main
print(listCharacters())

#Part 2:
import datetime
def getBios():
    people=csv.DictReader(open("starwars.csv","r"))
    now=datetime.date.today()
    for entry in people:
        birth_parts=entry["birthday"].split("/")
        print(birth_parts)
        #print(birth_parts)
        birthday=datetime.date(int(birth_parts[2]),int(birth_parts[0]),int(birth_parts[1]))
        age = now - birthday
        print(entry["name"],"is played by",entry["character"],"and was born on",birthday.strftime("%B %d, %Y"),"and is",round(age.days/365),"years old")

#main
getBios()

