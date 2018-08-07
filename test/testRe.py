import unittest
#from gameData.downloadTroopData import downloadTroopData
import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData.downloadTroopData import downloadTroopData
import globalVar

for troop in range(len(globalVar.TROOPTYPE)):
  url = globalVar.TROOPURL + globalVar.TROOPTYPE[troop]
  re = downloadTroopData(url, troop)
  troopClass = re.classJudge(troop)
  troopName = re.nameJudge(troop)
  print('Data of ' + troopClass + '(' + troopName + '):')
  re.getContent(url)
