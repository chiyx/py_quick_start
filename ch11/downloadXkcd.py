#! python3

import requests, os, bs4

baseUrl = 'http://xkcd.com'
url = baseUrl
os.makedirs('xkcd', exist_ok = True)

# store comics in ./xkcd
while not url.endswith('#'):
    print('Downloading page %s... ' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic images.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image
        print('Downloading image %s... ' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd.
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
        # Get the Prev btton's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = baseUrl + prevLink.get('href')
print('Done')