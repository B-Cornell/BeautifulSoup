#A look at how the electoral college represents voters and what affects
#it has on voter behavior

import urllib2
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


#open wiki page with data for each state (population, electoral votes, etc...)
votespage = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population')
votesoup = BeautifulSoup(votespage, 'html.parser')
#open wiki page with data about each state's voting patterns
partypage = urllib2.urlopen('https://en.wikipedia.org/wiki/United_States_presidential_election,_2016')
partysoup = BeautifulSoup(partypage, 'html.parser')


#Here we do the basic find the electoral college votes per person
#Essentially this is how much your vote matters if everyone votes


#All the data we need is in a table on the wikipedia page
stateseatslist = []
statenameslist = []
for statenumber in range(52): #DC and Puerto Rico are in the list and currently not used
    statename = votesoup.find_all('td')[2+(11*statenumber)].a.text #state name
    statepop = votesoup.find_all('td')[3+(11*statenumber)].text.rstrip() #state population
    statepop = int(statepop.replace(',', '')) #string to int
    statehouse = list(votesoup.find_all('td')[6+(11*statenumber)])
    if statename != 'Puerto Rico' and statename != 'District of Columbia':
        statehouse = int(statehouse[1].rstrip()) #string to int
        stateseats = statehouse+2 #the number of electoral votes is the number of house seats plus 2
        seatpercap = float(stateseats)/float(statepop)
        stateseatslist.append(seatpercap) #creates a list of how many electoral college votes each person has in every state
        statenameslist.append(statename) #creates a list of all the state names

#Find ratio of each states votes/person to the smallest votes/person
stateseatslist = [state/min(stateseatslist) for state in stateseatslist]

#plot
plt.bar(np.arange(50), stateseatslist, .5)
plt.xticks(np.arange(50), statenameslist, rotation = 90)
plt.show()
#this shows the people in Wyoming have almost 4 times as many electoral college votes per person as in Texas


#The next section will break down electoral votes by winning political party

'''

for x in list(list(partysoup.find_all('table')[37])[1])[3:]:
    if len(list(x)) > 2:
        voters = list(x)[45].text
        if ',' in list(x)[1].text or '(' in list(x)[1].text:
            newish = []
            print list(x)[1].text
            exa = list(list(x)[1].text)
            q = 0
            while exa[q] != ',' and exa[q] != ' ':
                print exa[q]
                newish.append(str(exa[q]))
                print newish
                q += 1
            newish = ''.join(newish)
            print newish

        partystatename = list(x)[1].text
        demvotes = list(x)[9].text
        repvotes = list(x)[15].text
        print partystatename
        print voters
        print demvotes
        print repvotes
        print ''


#'''





#possible future endeavors
#How does the Electoral College affect each party
#does the electoral college affect voter turnout based on votes per capita
#Do swing states behave differently than entrenched states
#Add compatibility for split vote states
#How would Puerto Rico affect voter outcome
#Take in past election data and compare it to modern data
#How do voters get their information compared to the past elections and how has that changed voting behavior
