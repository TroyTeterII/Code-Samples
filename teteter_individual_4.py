#simple pig translator
def pl_translate(word):
    if len(word) <= 1:
        return word+"yay"
    pre = word[0]
    suf = word[1:]
   
    if pre.upper() == pre:
        cap = True
    else:
        cap = False
 
    pig = suf + pre.lower() + "ay"
    if cap:
        pig = pig[0].upper() + pig[1:]
    return pig
#main
#print (pl_translate("Please"))

#Part 1 write a function pl_line, takes a string of words returns a string
# translated into pig latin, space and puncuation preserved
linetest="Please Translate Me."
punct=";,':?.! "
def pl_line(entry):
    #sort out punctuation
    for char in entry:
        if char in punct:
            print(entry.index(char))
            #doesn't work, i don't know what to do !!
    #split words apart in string
    orig_line=entry.split()
    #print(orig_line)
    #translate isolated words
    new_line=[]
    for item in orig_line:
        #print(item)
        new_word=pl_translate(item)
        new_line.append(new_word)
        trans_line=" ".join(new_line)
    return trans_line

#main
#print(pl_line(linetest))

#Part 2: define function that takes orginal file and an output file
# translates all words to pig latin
#writes into output file
def pl_file(orig_file,new_file):
    open_file=[line.split() for line in open(orig_file,"r")]
    print( open_file)
    trans=[pl_translate(item) for line in open_file for item in line]
    output_file=open(new_file,"a")
    for line in trans:
        output_file.write(line)
    return output_file 
#main
#print(pl_file("hw4tester.txt","newhwtester.txt"))


#Part 3: Give listing of text files in current working directory(cwd)
import os
home=os.getcwd()
print(home)
home_list=os.listdir(home)
txt_files=[]
for file in home_list:
    file=os.path.splitext(file)
    if file[1]==".txt":
        txt_files.append(file)
print(txt_files)

#User inputs file to translate to pig latin
userfile=input("enter a .txt file to translate to piglatin:")

#Create Directory Translations
path=os.path.join(home,"translations")
os.chdir(path)
print(os.getcwd())
#save output file in directory called 'translations'
#change name of file to [input_file_name](pig).txt
open_file=open(userfile,"w")
pl_file(userfile,userfile+"(PIG)")

#Part 4: Put current day and time at top of file
import datetime
now_date=datetime.datetime.today()
print(now_date)
open_file.seek(0)
open_file.write(str(now_date))

#print "thanks for using Pig latin Generator" at end of file

open_file.seek(2)
open_file.write("Thanks For using Pig Latin Genrator!")
open_file.close()



