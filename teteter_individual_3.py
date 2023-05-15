#List comprehension of txt file
    #open file
    #seperate into seperate lines of text

file=input("Enter a file name:")
print("PART 1")
openfile=[line.split() for line in open(file,"r")]
print(openfile)
print("##########################################################")
print("PART 2")
vowels="AEIOU"
#output of every racer in proper format
for line in openfile:
    print(line[0],"has traveled",line[1],"miles")
print("###########################################################")
print("PART 3")
#Seperate list comprehension of names beginning with vowel
vowler=[item for line in openfile for item in line if item[0] in vowels]
    #rough draft of comprehension
#vowelnames=[]
##for line in openfile:
##    for item in line:
##        print(item)
##        if item[0] in vowels:
##            vowelnames.append(item)
print("First names beginning with vowels:")
print(vowler)
##print(vowelnames)
print("##########################################################")
print("PART 5")
#3rd list comprehension of list of people traveling greater than 500 miles
    #rough draft of comprehension
##milenames=[]
##for item in openfile:
##    #print(item)
##    for things in item:
##        things=things.split()
##        for num in things:
##            if num.isdigit()and int(num)>500:
##                milenames.append(item)
##print(milenames)
miler=[item for item in openfile for things in item for num in things.split() if things.isdigit() and int(things)>500]
print(miler)
print("########################################################")
print("PART 6")
#display only names of people with over 500 miles
print("People traveled over 500 miles:")
for thing in miler:
    for num in thing:
        if num.isalpha():
            print(num)
        
