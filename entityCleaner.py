# init
import pandas as pd
from bs4 import BeautifulSoup

# settings
source = 'data/pages.xlsx'
sourceCol = 'excerpt'
target = 'data/clean-pages.xlsx'
targetCol = 'excerptNew'

# functions
def clean(text):
    cleaned = BeautifulSoup(text, 'lxml').get_text()
    return cleaned

# load data
pages = pd.read_excel(source)

# clean
pages[targetCol] = pages[sourceCol].apply(lambda x: clean(x))

pages.to_excel(target)
