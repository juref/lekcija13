#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'

vsebina = urlopen(url).read()
soup = BeautifulSoup(vsebina)

vsebina_filter = soup.findAll('table', {'class': 'wikitable plainrowheaders'})

vsebina_filter = soup.find('table', attrs={'class': 'wikitable plainrowheaders'})
linki = vsebina_filter.findAll('a', attrs={'href': re.compile('\/wiki\/Game_of_Thrones_\(season_?[0-9]+\)')})

ogledov = 0

for l in linki:
    temp_url = 'https://en.wikipedia.org' + l["href"]
    temp_vsebina = urlopen(temp_url).read()
    temp_soup = BeautifulSoup(temp_vsebina)
    temp_table = temp_soup.findAll('table', attrs={'class': 'wikitable plainrowheaders wikiepisodetable'})

    for row in temp_table:
        temp_row = row.findAll('tr')
        for col in temp_row:
            temp_col = col.findAll('td')
            if len(temp_col) == 6:
                cell = temp_col[-1].text
                val = cell[:4]
                if not val.isalpha():
                    # print val
                    ogledov = ogledov + float(val)

print 'Serijo "Game of Thrones" si je ogledalo ' + str(ogledov) + ' milijonov gledalcev'