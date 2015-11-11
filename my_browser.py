from search_engine import *

class My_Browser():
    def __init__(self,url_address, step):
        self.start_page = url_address
        self.step = step
        self.pages_list = []

    def page_not_added(self,page):
        return page not in self.pages_list


    def get_websites(self,url):
        if self.step != 0:
            new_pages = filter(self.page_not_added, extract_links(download_page(url)))
            self.step -=1
            self.pages_list.extend(new_pages)
            for page in new_pages:
                self.get_websites(page)
        else:
            return




