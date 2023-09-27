from urllib.request import urlopen
html = urlopen("html://www.google.com")
print(html.read())
