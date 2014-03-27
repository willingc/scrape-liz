#  Scraping demo using lxml and requests module
#
#  As described in Hitchhikers Guide to Python
#  http://docs.python-guide.org/en/latest/scenarios/scrape/
#-----------------------------------------------------------

# lxml library for processing xml and html
# http://lxml.de/
from lxml import html

# requests - a better library for http 
# http://docs.python-requests.org/en/latest/
import requests

# Get page and store data in the tree structure
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')


print 'Buyers: ', buyers
print 'Prices: ', prices


