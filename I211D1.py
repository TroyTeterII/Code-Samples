#step 1 get input from the user
#step 2 print input with underscores
#step 3 while loop with trackers and guesses
#step 4 check guess in word
#step 5 correct guess shown on board
#step 6 when board = word, game over

#Secret word
word=raw_input("Please enter a secred word:")

print word

#the board
board_word= ""
for i in word:
    if i ==" ":
        board_word += " "
    else:
        board_word += "_"
print board_word


used_letters = " "
moves=0


while word:


##Letters Used
    print "Your used letters:", used_letters 

##Number of moves
    print "Number of moves:", moves

#user guesses
    guess=raw_input("What's your guess?:")
    moves +=1
    used_letters+=guess

    new_board= ""

    for i in range(len(word)):
        if word[i] in used_letters:
            new_board +=word[i]
        else:
            new_board += "_"
    print new_board
    if new_board == guess:
        break
    

    
    

##Letters solved
