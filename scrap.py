#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen


url = 'https://scrapebook22.appspot.com/'

response = urlopen(url).read()
soup = BeautifulSoup(response)

vsi_trji = soup.findAll("tr")

vse_osebe = []

for tr in vsi_trji:
    ime = tr.find("td")
    vsi_tdji = tr.findAll("td")

    oseba = {
        "ime": "",
        "priimek": "",
        "email": "",
        "kraj": ""
    }

    if ime:
        oseba["ime"] = ime.string

    if vsi_tdji and len(vsi_tdji) > 1:
        priimek = vsi_tdji[1].string
        oseba["priimek"] = priimek

    if vsi_tdji and len(vsi_tdji) > 1:
        kraj = vsi_tdji[3].string
        oseba["kraj"] = kraj

    link = tr.find("a")

    if link and link.string == "See full profile":
        link_do_osebe = "https://scrapebook22.appspot.com" + link["href"]

        response2 = urlopen(link_do_osebe)
        soup2 = BeautifulSoup(response2)

        email = soup2.find("span", attrs={"class": "email"}).string
        oseba["email"] = email
        # print oseba

        vse_osebe.append(oseba)


# print vse_osebe

csv_data = open("podatki.csv", "w+")
for o in vse_osebe:
    csv_data.write(o["ime"] + "," + o["priimek"] + "," + o["email"] + "," + o["kraj"] + "\n")
    print "Done!"