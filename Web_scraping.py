

#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_txt = requests.get(url).text
s = BeautifulSoup(url_txt, 'lxml')
my_table = s.find_all('table', class_='wikitable sortable plainrowheaders')
table_links = my_table.find
print(tables)
