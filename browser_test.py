from my_browser import *

browser = My_Browser("http://www.bbc.com/",3)
print browser.pages_list
print browser.index["News"]
browser.find_websites("News")
print browser.index["you"]
browser.find_websites("you")