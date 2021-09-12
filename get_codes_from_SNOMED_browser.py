import bs4, requests
URL = "https://browser.ihtsdotools.org/?perspective=full&conceptId1=1148601009&edition=MAIN/2021-07-31&release=&languages=en"
res = requests.get(URL, allow_redirects=True)
res.raise_for_status()
open('SNOMED-Browser_sub.html', 'wb').write(res.content) #TODO fix : code content not extracted (i.e. 1148601009)

#bs4 not working
'''
soup = bs4.BeautifulSoup(res.text, 'html.parser')

try:
    elems = soup.select('title')  # working
    #elems = soup.select('#copy-content-custom') #TODO
except:
    print("CSS selector could not find element")
print(elems[0].text)
'''