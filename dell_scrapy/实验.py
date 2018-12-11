from urllib import request
import requests

haders = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
url = "http://music.163.com/song/media/outer/url?id=1321382056.mp3"

response = requests.get(url, headers=haders)
music = response.content
with open('music.mp3', 'ab') as f:
    f.write(music)