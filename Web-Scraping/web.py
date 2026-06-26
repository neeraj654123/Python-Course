import urllib.request ,urllib.parse,urllib.error

url = urllib.request.urlopen('http://google.com')

for line in url:
    print(line.decode().strip())