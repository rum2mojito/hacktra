from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv
import bs4


class getResource:
  def __init__(self, url):
    self.url = url
    self.reList = []

  def checkLink(self, url):
    try:
      r = requests.get(url)
      r.raise_for_status()
      r.encoding = r.apparent_encoding
      print("log in")
      #print(r.text)
      return r.text
    except:
      print('error in link server')

  def getContent(self, url):
    soup = BeautifulSoup(urlopen(url), 'lxml')
    trs = soup.find_all('tr')
    print("get table")
    for tr in trs:
      ui = []
      for td in tr:
        ui.append(td.string)
      self.reList.append(ui)

  def listFormat(self):
    tmpList = []
    start = 0
    col = 0
    for i in range(len(self.reList)):
      if self.reList[i][0] == '1':
        start = i
        break
    while(start < len(self.reList)):
      tmpList.append(self.reList[start][2*col])
      col += 1
      if(col == 5):
        col = 0
        start += 1
    print(tmpList)


