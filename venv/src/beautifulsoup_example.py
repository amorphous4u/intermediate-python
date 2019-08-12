from bs4 import BeautifulSoup

# URL for package : https://www.crummy.com/software/BeautifulSoup/
# python3 setup.py install - Inside the beautiful soup folder

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="brother" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="cousin" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


result = BeautifulSoup(html_doc, features="html.parser")
print(result.title)  # Get title of the html
print(result.title.name)
print(result.a) #Find url strings
print(result.find_all('a')) #Find all url strings

for link in result.find_all('a'):
    print(link.get('href')) # Print all href in the html

for link in result.find_all('a'):
    print(link.get('class')) # Print all class in the html