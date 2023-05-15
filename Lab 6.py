
import urllib.request,re
#Funciton to scrape all links from a webpage
web_page = urllib.request.urlopen("https://en.wikipedia.org/wiki/Category:Top_25_Report")
contents = web_page.read() .decode(errors="replace")
#contents=contents.replace('>','<').split('<')
web_page.close()
links=re.findall('["][\w]+["]',contents)

print(links[0:199])


