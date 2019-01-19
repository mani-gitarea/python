import requests
from bs4 import BeautifulSoup as bs
import os


# # Instagram retrieve photos into folder
url_insta = 'https://api.instagram.com/v1/users/self/media/recent?access_token=572036057.99a3992.71ae5eef47a84e2f8b784279156d65ad'

page = requests.get(url_insta)
data = page.json()['data']

if not os.path.exists('pictures/insta'):
    os.makedirs('pictures/insta')
else:
    for f in os.listdir('pictures/insta'):
        os.remove(os.path.join('pictures/insta',f))

os.chdir('pictures/insta')



x=0
for i in data:
   try:
       url = data[x]["images"]["standard_resolution"]["url"]
       picture = requests.get(url)
       if picture.status_code == 200:
           with open('picture' + str(x) + '.jpg','wb') as f:
              f.write(picture.content)
              f.close()
              x += 1
   except:
       pass

#Download Pictures from external site using HTML parsing

os.chdir("..")
if not os.path.exists('pexels'):
   os.makedirs('pexels')
else:
   for f in os.listdir('pexels'):
       os.remove(os.path.join('pexels', f))

os.chdir('pexels')

url_pexels = 'https://www.pexels.com/search/africa/'
page=requests.get(url_pexels)
soup = bs(page.text, 'html.parser')
image_tags = soup.findAll('img')

i=1

for image in image_tags:
    try:
        url = image["src"]
        picture = requests.get(url)
        if picture.status_code == 200:
            with open('picture' + str(i) + '.jpg','wb') as f:
                f.write(picture.content)
                f.close()
                i += 1
    except:
        pass
