from bs4 import BeautifulSoup
import urllib2

question = raw_input("Enter your query: ")
site = "http://www.google.com/search?q=" + question
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

req = urllib2.Request(site, headers=hdr)

try:
  page = urllib2.urlopen(req).read()
  soup = BeautifulSoup(page)
  a = soup.findAll('cite', attrs={'class': '_Rm'})
  for i in a:
    print
    print i.text
except urllib2.HTTPError, e:
  print e.fp.read()
