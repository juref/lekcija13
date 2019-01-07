#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ssl
import random

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://quotes.yourdictionary.com/theme/marriage/'

vsebina = urlopen(url).read()
soup = BeautifulSoup(vsebina)

vsi_citati = soup.findAll(attrs={"class": "quoteContent"})

i = 1


print "\nprvi način:\n"

while i < 6:
    print str(i) + '. citat: ' + random.choice(vsi_citati).string
    i += 1

print "\ndrugi način:\n"

izbor = random.sample(range(1, len(vsi_citati)), 5)
i = 1

for c in izbor:
    print str(i) + '. citat: ' + vsi_citati[c].string
    i += 1