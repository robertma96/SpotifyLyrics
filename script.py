import win32gui
import time
import urllib.request
import urllib
from bs4 import BeautifulSoup

songs = []
validation = True
song = ""
artist = ""


def getSong():
    global newSong, artist, song
    newSong = 0
    window_id = win32gui.FindWindow("SpotifyMainWindow", None)
    if window_id == 0:
        print("Start Spotify and then run the script again.")
        print("Press any key to EXIT")
        global validation
        validation = False
    song_info = win32gui.GetWindowText(window_id)
    temp = song_info
    try:
        global artist, song
        artist, song = temp.rsplit("-", 1)
        if len(songs) == 0:
            songs.append(song.rstrip)
        else:
            if songs[0] != song:
                print(artist + "-" + song.rstrip())
                newSong = 1
                del songs[0]
                songs.append(song)
    except ValueError:
        pass


def SongArtistGood(str_artist, str_song):

    global k, index, a, b
    k = 0
    index = 0
    a = str_artist.replace("The", "").lower().replace(" ", "").replace("'", "").replace(".", "").replace("-", "")\
        .replace("/", "")
    b = str_song.lower().replace(" ", "").replace("'", "").replace(".", "").replace("’", "").replace("!", "")\
        .replace(",", "").replace("?", "")
    for i in range(len(b)):
        if b[i] == "(":
            index = i
            while b[i] != ")":
                i = i + 1
                k = k + 1
            repl = b[index:index + k + 1]
            b = b.replace(repl, "")
            k = 0
            index = 0
            break
    for i in range(len(b)):
        if b[i] == "-":
            index = i
            while b[i] != b[-1]:
                if i == len(b):
                    k = len(b)
                    break
                i = i + 1
                k = k + 1
            repl = b[index:index + k + 1]
            b = b.replace(repl, "")
            k = 0
            index = 0
            break


def versuri(artist_bun, song_bun):
    try:
        no_scraped_page = "https://www.azlyrics.com/lyrics/" + artist_bun + "/" + song_bun + ".html"
        print(no_scraped_page)
        page = urllib.request.urlopen(no_scraped_page)
        soup = BeautifulSoup(page, 'html.parser')
        a = soup.find_all("div", attrs={'class': None})
        for res in a:
            print(res.text.strip())
    except:
        print("Nu am gasit versuri")
        print('\n')
    print('\n')


while validation:
    getSong()
    SongArtistGood(artist, song)
    time.sleep(.1)
    if newSong == 1:
        versuri(a, b)
