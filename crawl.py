'''
Web crawlser to search links in a site and links in the links of the search link ;>)
reference: Prof Mike McMillan
'''
import urllib, htmllib, formatter, re, sys

url = sys.argv[1] #write website
website = urllib.urlopen("http://"+url)
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
links =[]
links = ptext.anchorlist #grablinks
for link in links: # begin breathfirst search on each link
	if re.search('http', link) != None:
		print(link)
		website = urllib.urlopen(link)
		data = website.read()
		website.close()
		ptext = htmllib.HTMLParser(format)
		ptext.feed(data)
		morelinks = ptext.anchorlist #new links here
		for alink in morelinks: # search links in more links
			if re.search("http", alink) != None:
				links.append(alink)
