from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import globalVar
import logging
import env.logConfig


class downloadTroopData:
  def __init__(self, url, troopNum):
    self.url = url
    self.logger = logging.getLogger('downloadTroopData.py')
    self.reList = []
    self.troopNum = troopNum

  def getContent(self, url):
    try:
      r = requests.get(url)
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
      startTable1 = 0
      startTable2 = 0
      listTable2 = []

      for i in range(len(self.reList)):
        if self.reList[i][0] == 'Research':
          startTable1 = i
        if self.reList[i][0] == '1':
          startTable2 = i
          break

      listTable1 = self.getTable1(startTable1)
      if(globalVar.TROOPTYPE[self.troopNum] == '210' or globalVar.TROOPTYPE[self.troopNum] == '211'
          or globalVar.TROOPTYPE[self.troopNum] == '221' or globalVar.TROOPTYPE[self.troopNum] == '222'
          or globalVar.TROOPTYPE[self.troopNum] == '232'or globalVar.TROOPTYPE[self.troopNum] == '233'):
        print(listTable1)
        #return listTable1, listTable2
        return True
      else:
        listTable2 = self.getTable2(startTable2)
      print(listTable1)
      print(listTable2)
      return True
    except Exception as err:
      self.logger.error(err)
      return False

  def getTable1(self, startRow):
    try:
      listTable = []
      col = 0

      while(startRow < 7):
        if(startRow < 5):
          listTable.append(self.reList[startRow][2 * col])
          col += 1
          if (col == 7):
            col = 0
            startRow += 1
        else:
          listTable.append(self.reList[startRow][2 * col])
          col += 1
          if (col == 2):
            col = 0
            startRow += 1
      return listTable
    except Exception as err:
      self.logger.error(err)
      return  False

  def getTable2(self, startRow):
    try:
      listTable = []
      col = 0

      while (startRow < len(self.reList)):
        listTable.append(self.reList[startRow][2 * col])
        col += 1
        if (col == 7):
          col = 0
          startRow += 1
      return listTable
    except Exception as err:
      self.logger.error(err)
      return False

  def classJudge(self, troop):
    if((globalVar.TROOPTYPE[troop] >= '203' and globalVar.TROOPTYPE[troop] <='211') or globalVar.TROOPTYPE[troop] == '7'):
      troopClass = 'Gauls'
    elif globalVar.TROOPTYPE[troop] <= '222':
      troopClass = 'Romans'
    else:
      troopClass = 'Teutons'
    return troopClass

  def nameJudge(self, troop):
    try:
      Guals = ['Phalanx', 'Swordsman', 'Pathfinder', 'Theutates Thunder', 'Druidrider',
               'Haeduan', 'Ram', 'Trebuchet', 'Chieftain', 'Settler']
      Romans = ['Legionnaire', 'Praetorian', 'Imperian', 'Equites Legati', 'Equites Imperatoris',
                'Equites Caesaris', 'Battering Ram', 'Catapult', 'Senator', 'Settler']
      Teutons = ['Clubswinger', 'Spearman', 'Axeman', 'Scout', 'Paladin', 'Teutonic Knight',
                 'Ram', 'Catapult', 'Chief', 'Settler']
      troopName = ''

      if(self.classJudge(troop) == 'Gauls'):
        if(globalVar.TROOPTYPE[troop] == '7'):
          troopName = Guals[4]
        elif(globalVar.TROOPTYPE[troop] <= '206'):
          indexGauls = int(globalVar.TROOPTYPE[troop]) - 203
          troopName = Guals[indexGauls]
        elif(globalVar.TROOPTYPE[troop] >= '207'):
          indexGauls = int(globalVar.TROOPTYPE[troop]) - 202
          troopName = Guals[indexGauls]
        else:
          print('error in Gauls')
      elif(self.classJudge(troop) == 'Romans'):
        if(globalVar.TROOPTYPE[troop] == '212'):
          troopName = Romans[0]
        else:
          indexRomans = int(globalVar.TROOPTYPE[troop]) - 214
          troopName = Romans[indexRomans]
      elif(self.classJudge(troop) == 'Teutons'):
        indexTeutons = int(globalVar.TROOPTYPE[troop]) - 224
        troopName = Teutons[indexTeutons]
      else:
        print('error in nameJudge')
      return troopName
    except Exception as err:
      self.logger.error(err)
      return False
