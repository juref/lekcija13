#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://quotes.yourdictionary.com/theme/marriage/'

vsebina = urlopen(url).read()
soup = BeautifulSoup(vsebina)

vsi_citati = soup.findAll(attrs={"class": "quoteContent"})

citati = vsi_citati[:5]

for c in citati:
    print c.string