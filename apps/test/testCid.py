import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData.downloadTroopData import downloadTroopData
import globalVar
from dist.troop import troop

cid = '20'
url = globalVar.TROOPURL + globalVar.TROOPTYPE[cid]
re = downloadTroopData(url, cid)
troopClass = re.classJudge(cid)
troopName = re.nameJudge(cid)
print('Data of ' + troopClass + '(' + troopName + '):')
re.getContent(url)
print(troop.trainTime)