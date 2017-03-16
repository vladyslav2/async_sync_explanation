import requests
import sys


def fetch(url, counter):
    resp = ''
    for x in range(0, counter):
        resp = requests.get(url).text.encode('utf8')
    return resp;

def main():

    counter = 1
    try:
        counter = int(sys.argv[1])
    except:
        pass

    html = fetch('https://webdevelop.pro/', counter)
    print(html)

if __name__ == '__main__':
    main()
