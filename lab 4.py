
#list compehension to read a file
##file=input("please enter 'Cap.txt':")
##openfile=[line.split() for line in open(file,"r")]
####for line in openfile:
####    pass
####    #print(line)
##
#####strip whitesapces
##whitestrip=[item.strip() for line in openfile for item in line]
####for line in whitestrip:
####    pass
####    #print(line)
##
###convert to .lower()
##lower=[line.lower() for line in whitestrip for item in line]
####for line in lower:
####    #print(line)
####    pass
##
###remove puncuation
##import string
####for line in openfile:
####    for item in line:
####        if item in string.punctuation:
####            item
####            pass
##
##puncuator="".join([line for line in lower for item in line if item not in string.punctuation])
##print(puncuator)
###for line in puncuator:
###    print(line)
###Dictionary comprehension, words as keys
##
###counts are values for words occuring more than 100 times  (set(list_name)

#Problem 2

#request a file size, in Bytes
size=input("Choose a size of file, in Bytes:")
openfile=[

#print two list comprehensions
    #all files smaller than threshold

    #all file equal or greater than threshold

#rename files
    #small has "small" added to the name

    #larger has "large" added to the name
