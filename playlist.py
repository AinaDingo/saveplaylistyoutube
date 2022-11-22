import re
from pytube import Playlist

plist = input("link playlist: ")
playlist = Playlist(plist)
DOWNLOAD_DIR = 'path to save your video'

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=DOWNLOAD_DIR)