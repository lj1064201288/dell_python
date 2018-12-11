import socks
import socket
from urllib import request
from urllib.error import URLError

socks.set_default_proxy(socks.SOCKS5, '175.148.72.219', '1133')
socket.socket = socks.socksocket

try:
    response = request.urlopen('https://www.58.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)