from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

decades = ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
for decade in decades:
    page = "top_songs_of_the_{}".format(decade)
    url = 'http://www.musicvf.com/' + page

    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')

    soup = BeautifulSoup(''.join(data), "lxml")
    #print(soup.prettify())

    links = soup.find_all("p", style="margin-right: 0px;margin-left: 0px;margin-bottom: 0px;margin-top: 0px;font-size:18px")
    titles = []
    artists = []
    for link in links:
        song = link.get_text()
        song = song.replace(" by ", "|", -1)
        song = song.replace("é", "e")
        song = song.replace("ý", "y")
        song = song.replace("í", "i")
        if song[1] == "①" or song[1] =="②" or song[1] =="③" or song[1] =="④" or song[1] =="⑤":
            song = song[4:]
        title = song.split("|")[0].strip()
        artist = song.split("|")[1].strip()
        titles.append(title)
        artists.append(artist)

    df = pd.DataFrame({'Title': titles, 'Artist': artists})
    df.to_csv('{}.csv'.format(decade), index=False)

