import requests
from bs4 import BeautifulSoup
import json
url = "https://vcnewsdaily.com/archive.php"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


#to store and view source code
file = "content.html"
f_text= soup.prettify()
with open(file,"w+") as f:
    f.write(f_text)

#tp see the list of dates and links
dates=[]
anchors=[]

for d in soup.find_all('div',attrs={'class':'col-xl-9'}):
    date = d.find('div',attrs={'class' : 'row'}).text.replace('\n',' ')
    anchor=d.find_all('a',attrs={'class' :'d-block'})
    
dates.append(date)
anchors.append(anchor)


filename = 'result.json'                                          
with open(filename, 'w+') as file_object:                         
    json.dump(dates, file_object) 

#all images
for image in soup.find_all('img'):
    print(image.get('src'))


