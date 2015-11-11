import sys
import urllib2
from bs4 import BeautifulSoup
import re

reload(sys);
sys.setdefaultencoding("utf8")

def download_page(my_url):
    page = urllib2.urlopen(my_url)
    html = page.read()
    page.close()
    return html

def extract_links(html_as_str):
    soup = BeautifulSoup(html_as_str,"lxml")
    return [a['href'] for a in soup.find_all("a", href=True) if a['href'][0:4]=="http"]

def not_empty(element):
    if len(element)==0:
        return False
    elif element=="\n":
        return False
    return True

def visible(element):
    if element.parent.name in ['style','script','[document]','head','title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

def get_words(html_as_str):
    soup = BeautifulSoup(html_as_str,"lxml")
    text = soup.find_all(text=True)
    cleaned = [s.encode('utf-8') for s in filter(visible, text)]
    words=[]
    for i in cleaned:
        for word in i.split(" "):
            words.append(word)
    return filter(not_empty,words)

def word_frequency_dict(words_list):
    words_freq_dict = dict()
    for word in words_list:
        if word in words_freq_dict:
            words_freq_dict[word]+=1
        else:
            words_freq_dict[word]=1
    return words_freq_dict




bbc= download_page("http://www.bbc.com/")
print extract_links(bbc)
print word_frequency_dict(get_words(bbc))