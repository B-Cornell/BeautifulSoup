#eventually add in boundary cases maine and nebraska

import urllib2
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

votespage = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population')
votesoup = BeautifulSoup(votespage, 'html.parser')
partypage = urllib2.urlopen('https://en.wikipedia.org/wiki/United_States_presidential_election,_2016')
partysoup = BeautifulSoup(partypage, 'html.parser')



#Here we do the basic find the electoral college votes per person
#Essentially this is how much your vote matters if everyone votes
stateseatslist = []
statenameslist = []
for statenumber in range(52):
    statename = votesoup.find_all('td')[2+(11*statenumber)].a.text
    statepop = votesoup.find_all('td')[3+(11*statenumber)].text.rstrip()
    statepop = int(statepop.replace(',', ''))
    statehouse = list(votesoup.find_all('td')[6+(11*statenumber)])
    if statename != 'Puerto Rico' and statename != 'District of Columbia':
        stateparty = partysoup.find
        statehouse = int(statehouse[1].rstrip())
        stateseats = statehouse+2
        seatpercap = float(stateseats)/float(statepop)
        stateseatslist.append(seatpercap)
        statenameslist.append(statename)
plt.bar(np.arange(50), stateseatslist, .5)
plt.show()
#'''
