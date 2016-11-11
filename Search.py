'''
/ HAG Quick Search
/ Created by : Xploit
/ Date Created : 10/17/16
'''
from lxml import html
import requests
import sys
import re

def doSearch():
        print '\n[!] Welcome to Xploit\'s HAG Search [!]\n'
        gameName = raw_input('[!] Enter Game Name : ')
        gameName = re.sub('[ ]', '+', gameName)
        print '\n[!] Sending Request...\n'
        hagreq = requests.get('http://www.hackedarcadegames.com/search.php?q=%s' % gameName)
        hagtree = html.fromstring(hagreq.content)
	hagelement = hagtree.xpath('//ul[@class="game-row"]/li/p/a/span/text()')
	print '\n[!] Game Results [!]\n'
	print '\n'.join(hagelement)
        print '\n[!] Total Results : ', len(hagelement), '\n'
        SearchPrompt()

def SearchPrompt():
	answer = raw_input('Continue Searching? [Y/N] : ')
        if answer.lower() == 'y':
                return doSearch()
        if answer.lower() == 'n':
                sys.exit()
doSearch()
