#Part 1:
#First, prompt user to choose either rock, paper, or scissors
#second, The computer chooses from the 3 choices at random
#Program rules, Paper beats rock, Rock beats scissors, scissors beats paper
#check results for winner, or possible tie, tell the user the outcome


###Part 2:
##userWord=input("Enter a string to be reversed:")
##reverseWord=userWord[::-1]
##print(reverseWord)


#Part 3:
#asks user for 3 words
userWords=input("Enter Three Words, seperated by a space:")
#puts words in a list, unsorted

userList=userWords.split()

#new list of words sorted alphebetically
wordsSorted=userWords.split()

wordsSorted.sort()

print(userList)
print(wordsSorted)

#checks original list against sorted list
if userList==wordsSorted:
    print("true")
else:
    print("false")
