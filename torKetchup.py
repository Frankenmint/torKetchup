#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"/Users/frankenmint/Desktop/sideprojects/python/torrentKetchup/chromedriver")
browser.get('https://automatetheboringstuff.com')
