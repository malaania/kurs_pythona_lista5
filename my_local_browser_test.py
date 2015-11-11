from my_browser_local import *

browser = My_Browser()
print browser.pages_list
print browser.index["News"]
browser.find_websites("News")
print browser.index["you"]
browser.find_websites("you")