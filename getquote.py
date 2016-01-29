'''
Screen scrapping
reference: Prof Mike McMillan
'''
import urllib
import re
import sys

symbol = sys.argv[1]#get stock symbol form cmd
url = 'http://finance.google.com/finance?q='#set url for download
content = urllib.urlopen(url+symbol).read()#download it
m = re.search('span id ="ref.*>(.*)<', content)#seatch for location of stock quote
if m:#if match successfull retieve what is in that group
	quote = m.group(1)
else:#error
	quote = 'no quote for symbol: ' + symbol
print(quote)#print result		
