#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


def main():
    while True:
        showString = raw_input("\nWhat Show are we catching up on starting with episode # (ex: family guy S17E02)\n")
        
        if (showString == 'q'): 
           raise SystemExit

        endEpisode = raw_input("Which episode until we're caught up? (ex: 4, for episode 4)\n")

        # showString = "family guy S16E01"
        # endEpisode = "3"
        

        showSeason = showString.rsplit("E",1)[0]
        start = int(showString.rsplit("E",1)[1])
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=C:\\Users\\PUTYOURWINDOWSUSERNAMEHERE\\AppData\\Local\\Google\\Chrome\\User Data') #Path to your chrome profile
        # *NIX/OSX
        #options.add_argument('user-data-dir=/Users/User/Library/Application Support/Google/Chrome') #Path to your chrome profile
        options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(executable_path='%s/chromedriver.exe' % (os.getcwd()), options=options )
        for i in range (start, int(endEpisode)+1):
            lookup = showSeason+"E"+ str(i).zfill(2)
            try:
                browser.get('https://thepiratebay.org/')
                element = browser.find_elements_by_xpath('//*[@id="inp"]/input')[0]
                element.send_keys(lookup)
                element.submit()
                magnet = browser.find_elements_by_xpath('//*[@id="searchResult"]/tbody/tr[1]/td[2]/a')[0] #select the first magnet icon
                # print lookup
                # print magnet.get_attribute('href')
                magnet.click() #click the magnet icon href
            except IndexError:
                print "Unable to Find Torrent f0r %s" % (lookup)
            if (i == int(endEpisode)+1):
                browser.close()

        

if __name__ == "__main__":
    main()