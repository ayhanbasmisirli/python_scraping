from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.ankara.edu.tr")
bsobj = BeautifulSoup(html.read(),"html.parser")
print (bsobj.h2)
