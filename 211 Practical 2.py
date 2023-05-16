
#PART 1:  Parse website for 'news articles'
import re
import urllib.request
#open web page
web_page = urllib.request.urlopen("URL")
contents = web_page.read() .decode(errors="replace")
web_page.close()
#sort with regular expression
articles=re.findall('["][a-z]+["]?[>][\w ]+[:]?[,]?[\w ]+[0-9]?[.]?[<]',contents)
for entry in articles:
    #exclude extra text
    if 'headline' in entry:
        print(entry[11:-1])
        print('\n')

#Part 2: Parse web articles based on user search
#user search query
user_search=input("Please enter a word to search for:")
for entry in articles:
    #find articles on webpage
    if 'headline' in entry:
        #fine articles with search query
        if user_search in entry:
            print(entry[11:-1])
