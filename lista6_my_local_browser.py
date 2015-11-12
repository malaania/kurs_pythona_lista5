from search_engine import *
import threading

class Website(threading.Thread):
    def __init__(self,url, lock):
        self.url = url
        self.lock = lock
        threading.Thread.__init__(self)

    def run(self):
        print "Thread-"+self.url
        self.lock.acquire()
        print "Thread-"+self.url+" lock aqcuired"
        html = download_page(self.url)
        words_list  = get_words(html)
        print "Thread-"+self.url+" lock released"
        self.lock.release()
        self.words_freqency_dict = word_frequency_dict(words_list)
        print "Exiting Thread-"+self.url

class My_Browser():
    def __init__(self):
        self.pages_list = ['file:///home/malaania/UWr/websites/1.html',
                           'file:///home/malaania/UWr/websites/2.html',
                           'file:///home/malaania/UWr/websites/3.html',
                           'file:///home/malaania/UWr/websites/4.html',]
        self.index = self.__prepare_index()

    def __prepare_index(self):
        tuples_list= []
        lock = threading.Lock()
        threads_list = [Website(url, lock) for url in self.pages_list]
        for thread in threads_list:
            thread.start()
        for thread in threads_list:
            thread.join()
        for page in threads_list:
            tuples_list.append((page.url, page.words_freqency_dict))
        return index_pages(tuples_list)

    def find_websites(self, word):
        print "Welcome to mini browser!"
        print "You looked for the word '"+word+"'. Here are your search results:"
        web_index = 1
        for website in look_up_the_word(self.index,word):
            print str(web_index) + ". " +website
            web_index+=1