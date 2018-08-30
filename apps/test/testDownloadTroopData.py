import unittest
#from gameData.downloadTroopData import downloadTroopData
import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData.downloadTroopData import downloadTroopData
import globalVar

class testDownloadData(unittest.TestCase):
  def test_connection(self):
    for cid in sorted(globalVar.TROOPTYPE.keys()):
      url = globalVar.TROOPURL + globalVar.TROOPTYPE[cid]
      re = downloadTroopData(url, cid)
      troopClass = re.classJudge(cid)
      troopName = re.nameJudge(cid)
      #print('Data of ' + troopClass + '(' + troopName + '):')
      self.flag = False
      if (re.getContent(url) != False):
        self.flag = True
      self.assertEquals(self.flag, True)

if __name__ == '__main__':
  unittest.main()
