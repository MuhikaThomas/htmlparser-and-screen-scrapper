'''strips html tags
links indicated as numbers
no pictures
reference Prof Mike McMillan
'''
import htmllib
import urllib
import formatter
import sys

website = urllib.urlopen("http://www.profmcmillan.com")#open webpage
data = website.read()#read content
website.close()#close website
format = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))#fromatter to display text
ptext = htmllib.HTMLParser(format)#set parser
ptext.feed(data)#feed original html to ptext var
ptext.close()
