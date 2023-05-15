#The FUNCTIONING CODE is in 2 seperate files on my cgi-pub folder
#(teteter_individual_6.html and teteter_individual_6.cgi)
#The following are copies of the files with comments added. Thanks!

#teteter_individual_6.html   :

<html>
<head><title>First Interactive Form</title></head>
<body>

<form action="teteter_individual_6.cgi" method="post">
	Please enter your name:
        #User Phrase
	<input type="text" name="plainText"><br>
	#User key
	<input type="number" name="shift" min="0" max="26">
	#submit button
	<input type="submit" value="Submit">
</form> 

</body>
</html>

#teteter_individual_6.cgi   :

#! /usr/bin/env python
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Form in CGI</title></head>
    <body>
	<p>{content}</p>
    </body>
</html>"""
#Function that encodes a string based on a numerical key
def caesar(plainText, shift):
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
    return cipherText

try:
    #retrieve data from HTML form
    phrase=form.getfirst('plainText','0')
    key=int(form.getfirst('shift','0'))
    #pass data through caesar cipher function, display output
    print caesar(phrase,key)

except:
    print html.format(content='invalid')


