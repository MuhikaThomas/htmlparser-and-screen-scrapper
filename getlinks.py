'''
Listing links in a website plaintext
reference: Prof Mike McMillan
'''
import urllib
import htmllib
import formatter

website = urllib.urlopen("http://www.profmcmillan.com")
data = website.read()
website.close()
format =formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
for link in ptext.anchorlist:
 print(link)
