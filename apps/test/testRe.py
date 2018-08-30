import unittest
#from gameData.downloadTroopData import downloadTroopData
import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData.downloadTroopData import downloadTroopData
import globalVar
from dist.troop import troop
from metastore.dao.troopDataDAO import troopDataDAO

tmpDAO = troopDataDAO()
tmpDAO.createTroopTable()

for cid in sorted(globalVar.TROOPTYPE.keys()):
  url = globalVar.TROOPURL + globalVar.TROOPTYPE[cid]
  re = downloadTroopData(url, cid)
  troopClass = re.classJudge(cid)
  troopName = re.nameJudge(cid)
  print('Data of ' + troopClass + '(' + troopName + '):')
  re.getContent(url)
  print(troop.name)
  re.writeDB(troop, tmpDAO)

tmpDAO.__del__()