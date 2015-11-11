from my_browser import *

browser = My_Browser("http://www.bbc.com/",2)
print browser.pages_list
print len(browser.pages_list)
print len(browser.index)