from urllib2 import HTTPError
from search_engine import *

class My_Browser():
    def __init__(self,url,num_links):
        self.pages_list = [url] + extract_links(download_page(url))[0:num_links]
        self.index = self.__prepare_index()

    def __prepare_index(self):
        tuples_list= []
        for page in self.pages_list:
            tuples_list.append(self.__prepare_tuple(page))
        return index_pages(tuples_list)

    def __prepare_tuple(self, page):
        return (page,word_frequency_dict(get_words(download_page(page))))

    def find_websites(self, word):
        print "Welcome to mini browser!"
        print "You looked for the word '"+word+"'. Here are your search results:"
        web_index = 1
        for website in look_up_the_word(self.index,word):
            print str(web_index) + ". " +website
            web_index+=1