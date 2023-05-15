##import os
###make directory
##os.makemydir("new_directory")
###list directories
##pylist=[file for file in os.listdir(os.getcwd()) if ".py" in file]
##print(pylist)
###Remove directory
##os.remove("new_directory")

table= '<table border=1>'

for i in range(32):
    table += '<tr>'
    for o in range(11):
        table +='<td>row' +str(i+1)+' Col'+str(0+i)+'</td>'


html= """<!doctiype hmtl>
<html>
<head>
	<meta charset="utf-8">
	<title>CGI table</title>
</head>

<body>
	<h1>CONTENT OF THE PAGE</h1>
	
</body>
</html>
"""
#print(table)

#GET FILE TO RUN ON HMTL BROWSER:
out.write(html.format(content=table)
