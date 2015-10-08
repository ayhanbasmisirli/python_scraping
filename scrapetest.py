from urllib.request import urlopen
html = urlopen("http://www.ankara.edu.tr")
print(html.read())
