from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import globalVar
import logging
import re
from dist.troop import troop
import env.logConfig

class downloadTroopData:
  def __init__(self, url, troopNum):
    self.url = url
    self.logger = logging.getLogger('downloadTroopData.py')
    self.reList = []
    self.troopNum = troopNum

  def getElement(self, text, pattern):
    match = re.findall(pattern, text)
    return match

  def getContent(self, url):
    try:
      r = requests.get(url)
      soup = BeautifulSoup(urlopen(url), 'lxml')
      trs = soup.find_all('tr')
      for tr in trs:
        self.ui = []
        for td in tr:
          self.ui.append(td.string)
        self.reList.append(self.ui)
      #print(self.reList)
      return self.writeToTroop()
    except Exception as err:
      self.logger.error(err)
      return False

  def listFormat(self):
    try:
      startAttack = 0
      startTable1 = 0
      startTable2 = 0
      endTable1 = 0
      listTable2 = []

      for i in range(len(self.reList)):
        if self.reList[i][0] == 'Value at troop level 0':
          startAttack = i
        if self.reList[i][0] == 'Research':
          startTable1 = i
        if self.reList[i][0] == 'Can carry':
          endTable1 = i
        if self.reList[i][0] == '1':
          startTable2 = i
          break

      listAttack = self.getAttack(startAttack)

      listTable1 = self.getTable1(startTable1, endTable1)
      if(globalVar.TROOPTYPE[self.troopNum] == '210' or globalVar.TROOPTYPE[self.troopNum] == '211'
          or globalVar.TROOPTYPE[self.troopNum] == '221' or globalVar.TROOPTYPE[self.troopNum] == '222'
          or globalVar.TROOPTYPE[self.troopNum] == '232'or globalVar.TROOPTYPE[self.troopNum] == '233'):
        #print(listTable1)
        #print(listTable1)
        return listTable1, listTable2, listAttack
      else:
        listTable2 = self.getTable2(startTable2)
      '''print(listTable1)
      print(listTable2)'''
      #print(listTable1)
      return listTable1, listTable2, listAttack
    except Exception as err:
      self.logger.error(err)
      return False

  def writeToTroop(self):
    try:
      startRes = 0
      startTraining = 0
      startVel = 0
      startCarry = 0

      (listTable1, listTable2, listAttack) = self.listFormat()
      # print(len(listTable2))
      for ele in range(len(listTable1)):
        if(listTable1[ele] == 'Research'):
          startRes = ele + 1
        elif(listTable1[ele] == 'Training' or listTable1[ele] == 'Training (T3.5) '):
          startTraining = ele +1
        elif(listTable1[ele] == 'Velocity'):
          startVel = ele +1
        elif(listTable1[ele] == 'Can carry'):
          startCarry = ele + 1
          break

      #read tablel1 research
      (troop.resLumber, troop.resClay, troop.resIron, troop.resCrop, troop.xCropRes, troop.resTime) = listTable1[startRes:startRes+6]
      troop.resLumber = int(troop.resLumber)
      troop.resClay = int(troop.resClay)
      troop.resIron = int(troop.resIron)
      troop.resCrop = int(troop.resCrop)
      if(troop.xCropRes == '/'):
        troop.xCropRes = 0
      else:
        troop.xCropRes = int(troop.xCropRes)
      if(troop.resTime == '/'):
        troop.resTime = 0
      else:
        troop.resTime = self.timeToSecond(troop.resTime)

      #read table1 training
      (troop.trainLumber, troop.trainClay, troop.trainIron, troop.trainCrop, troop.xCropTrain, troop.trainTime) = listTable1[startTraining:startTraining+6]
      troop.trainLumber = int(troop.trainLumber)
      troop.trainClay = int(troop.trainClay)
      troop.trainIron = int(troop.trainIron)
      troop.trainCrop = int(troop.trainCrop)
      if (troop.xCropTrain == '/'):
        troop.xCropRes = 0
      else:
        troop.xCropTrain = int(troop.xCropTrain)
      if (troop.resTime == '/' or troop.resTime == None):
        troop.resTime = 0
      else:
        troop.trainTime = self.timeToSecond(troop.trainTime)

      #read table1 velocity & carry
      troop.velocity = listTable1[startVel]
      troop.carry = listTable1[startCarry]
      troop.velocity = int(troop.velocity[0])
      versionFlag = 0
      for ele in range(len(troop.carry)):
        if(troop.carry[ele] == '/'):
          versionFlag = 1
          slash = ele
          break
      if(versionFlag == 1):
        troop.carry = int(troop.carry[slash+1] + troop.carry[slash+1])
      else:
        troop.carry = int(troop.carry[0])

      #read table2
      level = [0] * 20
      lumber = [0] * 20
      clay = [0] * 20
      iron = [0] * 20
      crop = [0] * 20
      timeL1 = [0] * 20
      timeL2 = [0] * 20
      if(len(listTable2) == 0):
        return level, lumber, clay, iron, crop, timeL1, timeL2
      else:
        for row in range(20):
          if(level[row] == None):
            level[row] = 0
          else:
            level[row] = int((listTable2[7*row]))
          if (listTable2[7 * row + 1] == None):
            lumber[row] = 0
          else:
            lumber[row] = int(listTable2[7 * row + 1])

          if(listTable2[7*row + 2] == None):
            clay[row] = 0
          else:
            clay[row] = int(listTable2[7*row + 2])

          if (listTable2[7 * row + 3] == None):
            iron[row] = 0
          else:
            iron[row] = int(listTable2[7*row + 3])

          if(listTable2[7*row + 4] == None):
            crop[row] = 0
          else:
            crop[row] = int(listTable2[7*row + 4])

          if(listTable2[7 * row + 5] == None):
            timeL1[row] = 0
          else:
            timeL1[row] = self.timeToSecond(listTable2[7*row + 5])

          if(listTable2[7*row + 6] == None) :
            timeL2[row] = 0
          else:
            # skip \xa0
            timeStr = listTable2[7 * row + 6]
            timeStr = "".join(timeStr.split())
            if (len(timeStr) == 0):
              timeL2[row] = 0
            else:
              timeL2[row] = self.timeToSecond(timeStr)
      return True
    except Exception as err:
      self.logger.error(err)
      return False

  def timeToSecond(self, time):
    try:
      hour = 0
      minute = 0
      second = 0
      lenTime = len(time)
      for ele in range(lenTime):
        if(time[ele] == ':' and (lenTime-ele) == 6):
          colonFirst = ele
        elif(time[ele] == ':' and (lenTime-ele) == 3):
          colonSecond = ele

      if (colonFirst == 1):
        hour = int(time[0])
      elif (colonFirst == 2):
        hour = int(time[0] + time[1])
        minute = int(time[colonFirst + 1] + time[colonFirst + 2])
        second = int(time[colonSecond + 1] + time[colonSecond + 2])

      seconds = 3600*hour + 60*minute +second
      return seconds
    except Exception as err:
      self.logger.error(err)
      return False

  def getAttack(self, startRow):
    try:
      listAttack = []
      for col in range(4):
        listAttack.append(self.reList[startRow][2 * col])
      return listAttack
    except Exception as err:
      self.logger.error(err)
      return False

  def getTable1(self, startRow, endRow):
    try:
      listTable = []
      col = 0
      startOriginal = startRow

      if(endRow - startOriginal == 3):
        startBias = 2
      elif(endRow - startOriginal == 4):
        startBias = 3

      while (startRow < endRow + 1):
        if(startRow < startOriginal + startBias):
          if(self.reList[startRow][0] == 'Training (T2.5) '):
            #jump to next row
            startRow += 1
          else:
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
      return False

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
          indexRomans = int(globalVar.TROOPTYPE[troop]) - 213
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
