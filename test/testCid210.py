import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData.downloadTroopData import downloadTroopData
import globalVar

troop = 8
cid = globalVar.TROOPTYPE[troop]

url = globalVar.TROOPURL + cid
re = downloadTroopData(url, troop)
troopClass = re.classJudge(troop)
troopName = re.nameJudge(troop)
print('Data of ' + troopClass + '(' + troopName + '):')
re.getContent(url)