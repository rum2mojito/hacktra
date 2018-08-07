import unittest
#from gameData.downloadTroopData import downloadTroopData
import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData.downloadTroopData import downloadTroopData
import globalVar

class testDownloadData(unittest.TestCase):
  def test_connection(self):
    for troop in range(len(globalVar.TROOPTYPE)):
      url = globalVar.TROOPURL + globalVar.TROOPTYPE[troop]
      re = downloadTroopData(url, troop)
      troopClass = re.classJudge(troop)
      troopName = re.nameJudge(troop)
      #print('Data of ' + troopClass + '(' + troopName + '):')
      self.flag = False
      if(re.getContent(url) != False):
       self.flag = True
      self.assertEquals(self.flag, True)

if __name__ == '__main__':
  unittest.main()