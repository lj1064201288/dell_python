import requests

if __name__ == '__main__':

    r = requests.get('http://www.httpbin.org/get')
    print(r.text)

