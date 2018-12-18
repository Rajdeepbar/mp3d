import urllib.request
from bs4 import BeautifulSoup
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',   
    }],
    'noplaylist': True, 
}


# export the https proxy environment variables
class find:
    def load(self,name, option):
        query = urllib.parse.quote(name)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        url, title,minutes,seconds = [],[],[],[]
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            url.append('https://www.youtube.com' + vid['href'])
            title.append(vid['title'])
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for i in range(option):
                info_dict = ydl.extract_info(url[i],download=False)
                time = str(float(info_dict["duration"]/60))
                minutes.append(time.split(".")[0])
                seconds.append(str(int(int(str(int(time.split(".")[1]))[:2])*0.6)))
        return url,title,minutes,seconds




