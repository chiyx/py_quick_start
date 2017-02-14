#! python3

# lucky.py - opens several Google search results

import requests
import sys
import webbrowser
import bs4

print('Googling... ')
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElems = soup.select('#search .r a')
numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))






