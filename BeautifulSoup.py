from bs4 import BeautifulSoup

with open('1.xml','r') as f:
        rawdata = f.read()
data = BeautifulSoup(rawdata,"xml")
print(data.get_text())
