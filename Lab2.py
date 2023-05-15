###Task 1
##doubles=[(x*2)for x in range(10)]
##print(doubles)

###Task 2
##numbers=[x for x in range(100) if x%10==0]
##print(numbers)

###Task 3
##words=["appple","ball","candle","dog","egg","frog"]
###list comprehension
##words=[words[i].upper() if len(words[i])<4 else words[i] for i in range(len(words)) ]
##print(words)

#Task 4
#takes input from user
secret=input("Please enter the secret:")
#loops through string, changing lettes to dashes
secret=["-" if letter.isalpha()else letter for letter in secret]
new="".join(secret)
#reprints the string
print(new)
