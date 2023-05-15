import xml.etree.ElementTree as ET
from tools import *

##Part 1: CD Catalog
##Your mission will be to do the following:

##Download the cd_catalog.xml file. This XML document contains records for CDs.
##The root element is CATALOG and contains a series of CD elements, each of which
##has a number of child elements such as TITLE, PRICE and so on.
 
##Write a program that will read the file and print out the following information
##with an appropriate message:
##a.   (10 points) The total number of CDs in the file and the total price of
##                 purchasing one of each.
##b.   (10 points) The minimum, maximum, and average price for the CDs in the file.
##c.   (10 points) The titles of all CDs released in the year 1987.
##d.   (10 points) Print the names of all artists who released a record through Columbia.
##e.    bonus +5   Use list comprehensions to minimize the code required in parts a – d.



import xml.etree.ElementTree as ET
from tools import *

#function for removing duplicates in a list
def remove_duplicates(values):
    output = []
    seen = set()
    #list comprehension:
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
##            output.append(value)
            seen.add(value)
    output = [value for value in values if value not in seen]
    return seen

#open XML doc, view elements
root = ET.parse('cd_catalog.xml')
print(root)

elements = root.iter()

##for elem in elements:
##    print("Tag Name:", elem.tag)
##    print("Tag Text:", elem.text)
##    print("Children:", list(elem))
##    print("-"*20)

#Total number of CD's, total purchasing price for all
count=0

for elem in elements:
    count+=1
    
prices = root.findall("CD/PRICE")

total = 0.0

for elem in prices:
    price = elem.text
    total+=float(price)
    
print('Total number of CDs:',count,'Total purchasing price:',int(total))

#Min, Max, and Avg price of CDS
price_list = []
#list comp:
price_list = [elem.text for elem in prices]
##for elem in prices:
##    price_list.append(elem.text)
    
print(price_list)

print(len(price_list))

avg = total/len(price_list)

print('Min:',price_list[-3],'Max:',price_list[0],'Average Price:','$', avg)


#Titles of all CDs, in the year 1987
cd_title = root.findall("CD/TITLE")

cd_year = root.findall("CD/YEAR")

book_titles = []
#list comp:
book_titles = [title.text for title in cd_title for year in cd_year if year.text == '1987']
##for title in cd_title:
##    for year in cd_year:
##        if year.text == '1987':
##            book_titles.append(title.text)

print("Books released in 1987:",remove_duplicates(book_titles))



#Names of artists with Columbia records
cd_artist = root.findall("CD/ARTIST")

cd_company = root.findall("CD/COMPANY")

artist_list = []
#list comp:
artist_list = [artist.text for artist in cd_artist for comp in cd_company if comp.text == 'Columbia']
##for artist in cd_artist:
##    for comp in cd_company:
##        if comp.text == 'Columbia':
##            artist_list.append(artist.text)
print("Authors under Columbia Publishing:",remove_duplicates(artist_list))



##Part 2: Book Catalog
##Your mission will be to do the following:
##
##Download the books.xml file. The root element is CATALOG and contains a series of
##BOOK elements, each of which represents a single BOOK.
##Each BOOK element has a number of child elements such as AUTHOR, TITLE, GENRE,
##PRICE and so on.
##
##Write a program to read the file and print out the following information with an
##appropriate message:
##a.   (15 points) Write a function called book_info that prints the title, author,
##                 and price of the book with a certain id (passed as a parameter).
##                 Build a list of all book ids in the XML file and call this function
##                 on each of them. Example call: book_info(“bk111”)
##b.   (10 points) Print the total number of Fantasy books released in November.
##c.   (10 points) Print the unique genres in the file.
##e.   (10 points) Use list comprehensions to minimize the code required in parts a – b.
##f.    bonus + 5  Use list comprehensions AND dictionary comprehensions to minimize the
##                 code required in part c.



##a.   (15 points) Write a function called book_info that prints the title, author,
##and price of the book with a certain id (passed as a parameter).
##Build a list of all book ids in the XML file and call this function on each of them.
##Example call: book_info(“bk111”)

print('-'*77,'\n'+'-'*77)

listid = ['bk101', 'bk102', 'bk103', 'bk104', 'bk105', 'bk106',\
       'bk107', 'bk108', 'bk109', 'bk110', 'bk111', 'bk112']

def book_info(ID):
    root2 = ET.parse('books.xml')
    books = root2.iter('book')

    for book in books:

        if book.attrib['id'] == ID:
        
            print ('\nID Number Called: '+str(book.attrib['id'])+'\n'+\
                   '\nTitle: '+str(book.find('title').text)+'\n'+\
                   'Author: '+str(book.find('author').text)+'\n'+\
                   'Price: $'+str(book.find('price').text)+'\n\n'+'-'*77)

for ID in listid:
    book_info(ID)




##b.   (10 points) Print the total number of Fantasy books released in November.

root2 = ET.parse('books.xml')
books = root2.iter('book')

fantasy = []
#list comp:
##fantasy = [gendate for book in books if book.find('genre').text == 'Fantasy': gendate = (book.find('genre').text+' '+book.find('publish_date').text)]
##for book in books:
##
##    if book.find('genre').text == 'Fantasy':
##        gendate = (book.find('genre').text+' '+book.find('publish_date').text)
##        fantasy.append(gendate)


count=0

for item in fantasy:
    if item[13:15] == '11':
        count+=1

print('-'*77,'\n'+'\nThe total number of Fantasy books released in November:',\
      str(count)+'\n\n'+'-'*77,'\n'+'-'*77,'\n')



##c.   (10 points) Print the unique genres in the file.

root2 = ET.parse('books.xml')
books = root2.iter('book')

genres = []
dups = set()

print('The unique genres of books are:\n')

for book in books:

    if book.find('genre').text not in dups:
        print(book.find('genre').text)
        dups.add(book.find('genre').text)

print('\n'+'-'*77,'\n'+'-'*77,'\n')



##e.   (10 points) Use list comprehensions to minimize the code required in parts a – b.




##f.   bonus + 5   Use list comprehensions AND dictionary comprehensions to minimize the
##     code required in part c.
