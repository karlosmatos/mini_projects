from pytube import YouTube
import os

def url_receiver():
    urls = list(map(str, input('Insert YT urls to download as MP3: ').split())) #URL receiver
    return urls

def get_file_direction():
    file_direction = input('Give me path to your downloads (example: "/content/YT downloads") ') #file direction
    return file_direction

class YoutubeMP3Downloader:

    def __init__(self, urls, file_direction):
        self.file_direction = file_direction
        self.urls = urls

    def urls_download(self):
        for count, url in enumerate(self.urls):
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(self.file_direction)
            base, ex = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            print(f"Video #{count}: Done")

def main():
    urls = url_receiver()
    file_direction = get_file_direction()
    ytb_download = YoutubeMP3Downloader(urls, file_direction)
    ytb_download.urls_download()

if __name__ == '__main__':
    main()
