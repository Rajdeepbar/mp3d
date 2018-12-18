import Search
import Download

class MP3D:

    # search takes the input name of the audio and returns a list of title of various videos
    def search(self,name,option):   
        audio = Search.find()
        self.url, self.title, minutes, seconds = audio.load(name,option)
        return self.title, minutes, seconds

    # download takes the number of the video to be downloaded and starts the download
    def download(self,option):
        object = Download.download(self.url,self.title)
        check = object.start(option)
        return check


