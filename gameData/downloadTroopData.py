from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import logging

import env.logConfig

class downloadTroopData:
  def __init__(self, url):
    self.url = url
    self.logger = logging.getLogger('downloadTroopData.py')
    self.reList = []

  def checkLink(self, url):
    try:
      r = requests.get(url)
      r.raise_for_status()
      r.encoding = r.apparent_encoding
      self.logger.debug('Initial ' + url)
      # return r.text
    except Exception as err:
      self.logger.error(err)

  def getContent(self, url):
    try:
      soup = BeautifulSoup(urlopen(url), 'lxml')
      trs = soup.find_all('tr')
      for tr in trs:
        ui = []
        for td in tr:
          ui.append(td.string)
        self.reList.append(ui)
      return self.listFormat()
    except Exception as err:
      self.logger.error(err)
      return False

  def listFormat(self):
    try:
      tmpList = []
      start = 0
      col = 0
      for i in range(len(self.reList)):
        if self.reList[i][0] == '1':
          start = i
          break
      while (start < len(self.reList)):
        tmpList.append(self.reList[start][2 * col])
        col += 1
        if (col == 5):
          col = 0
          start += 1
      self.logger.debug('finished')
      return True
    except Exception as err:
      self.logger.error(err)
      return False

# if __name__ == '__main__':
#   url = "https://t4.answers.travian.com/index.php?view=answers&action=answer&cid=203"
#   re = downloadTroopData(url)
#   #re.checkLink(url)
#   re.getContent(url)
#   # print(re.reList)
#   #re.listFormat()
