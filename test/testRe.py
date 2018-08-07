import unittest
#from gameData.downloadTroopData import downloadTroopData
import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData.downloadTroopData import downloadTroopData
import globalVar

for cid in sorted(globalVar.TROOPTYPE.keys()):
  # url = globalVar.TROOPURL + globalVar.TROOPTYPE[troop]
  url = globalVar.TROOPURL + globalVar.TROOPTYPE[cid]
  re = downloadTroopData(url, cid)
  troopClass = re.classJudge(cid)
  troopName = re.nameJudge(cid)
  print('Data of ' + troopClass + '(' + troopName + '):')
  re.getContent(url)
