import sys
import urllib2
from bs4 import BeautifulSoup
import re
import string

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
    punctuation_set = set(string.punctuation)
    soup = BeautifulSoup(html_as_str,"lxml")
    text = soup.find_all(text=True)
    cleaned = [s.encode('utf-8') for s in filter(visible, text)]
    words=[]
    for i in cleaned:
        for word in i.split(" "):
            word = ''.join(ch for ch in word if ch not in punctuation_set)
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

def index_pages(tuples_page_dict_list):
    word_on_page_dict = dict()
    for page, word_dict in tuples_page_dict_list:
        for word, freq in word_dict.iteritems():
            if word in word_on_page_dict:
                word_on_page_dict[word][page]=freq
            else:
                word_on_page_dict[word]={page:freq}
    return word_on_page_dict

def look_up_the_word(words_pages_dict, word):
    if word not in words_pages_dict:
        return "Sorry! No search result."
    else:
        result_dict = words_pages_dict[word]
        return sorted(result_dict, key=result_dict.__getitem__,reverse=True)

