import itertools
import re

def abbreviate(text):
    text = ''.join(text.split(':', 1)[0])
    text_re = re.findall('[A-Z][^A-Z]*', text)
    text_ = []
    for text in text_re:
        text_ += text.split()
    text_list = []
    for text in text_:
        text_list += text.split('-')
    return ''.join(text[0].upper() for text in text_list)
    
