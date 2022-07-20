from pytube import YouTube
import os

urls = list(map(str, input('Insert YT urls to download as MP3: ').split())) #URL receiver
for count, url in enumerate(urls):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    file_direction = '/content/YT downloads' #file direction
    downloaded_file = video.download(file_direction)
    base, ex = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    print(f"Video #{count}: Done")
