from urllib2 import HTTPError
from search_engine import *

class My_Browser():
    def __init__(self,url,num_links):
        self.pages_list = [url] + extract_links(download_page(url))[0:num_links]
        self.index = self.prepare_index()

    def prepare_index(self):
        tuples_list= []
        for page in self.pages_list:
            tuples_list.append(self.prepare_tuple(page))
        return index_pages(tuples_list)

    def prepare_tuple(self, page):
        return (page,word_frequency_dict(get_words(download_page(page))))








