import youtube_dl 

flag = 0

def my_hook(d):
    global flag
    if d['status'] == 'finished':
        flag = 1
    

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',   
    }],
    'noplaylist': True, 
    'progress_hooks': [my_hook],
}

class download():
    def __init__(self,url,title):
        self.url = url
        self.title = title  

    def start(self,name):
        global flag
        option = int(name)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url[option-1]])
        return flag           





