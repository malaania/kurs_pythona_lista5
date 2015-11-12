from lista6_my_local_browser import *

browser = My_Browser()
print browser.pages_list
print browser.index["News"]
browser.find_websites("News")
print browser.index["you"]
browser.find_websites("you")
browser.find_websites("tomato")