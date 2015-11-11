from search_engine import *

bbc= download_page("http://www.bbc.com/")
bbc_culture = download_page("http://www.bbc.com/culture/")
bbc_word_dict = word_frequency_dict(get_words(bbc))
bbc_culture_word_dict = word_frequency_dict(get_words(bbc_culture))
tuple_list = [("http://www.bbc.com/", bbc_word_dict),("http://www.bbc.com/culture/",bbc_culture_word_dict)]
indexed = index_pages(tuple_list)
print extract_links(bbc)
print word_frequency_dict(get_words(bbc))
print indexed["News"]
print look_up_the_word(indexed, "News")
print indexed["you"]
print look_up_the_word(indexed, "you")

