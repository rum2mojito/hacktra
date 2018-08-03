import unittest
#from gameData.downloadTroopData import downloadTroopData
import sys
sys.path.append('home/parallels/Downloads/hacktra/gameData')
from gameData import downloadTroopData
import globalVar

class test(unittest.TestCase):

  def test_connection(self):
    for troop in range(len(globalVar.TROOPTYPE)):
      url = globalVar.TROOPURL + globalVar.TROOPTYPE[troop]
      re = downloadTroopData.downloadTroopData(url, troop)
      troopClass = re.classJudge(troop)
      troopName = re.nameJudge(troop)
      print('Data of ' + troopClass + '(' + troopName + ')')
      re.getContent(url)
      if(re.getContent(url) != ''):
        self.flag = True
      self.assertEquals(self.flag, True)

if __name__ == '__main__':
  unittest.main()

'''import unittest

from gameData.downloadTroopData import downloadTroopData

class TestDAO(unittest.TestCase):
  def test_connection(self):
    troop = 0
    url = "https://t4.answers.travian.com/index.php?view=answers&action=answer&cid=203"
    re = downloadTroopData(url, troop)
    re.getContent(url)
    #self.assertEquals(re.getContent(url), True)
    if(re.getContent(url) != ''):
      self.flag = True
    self.assertEquals(True, self.flag)

if __name__ == '__main__':
  unittest.main()'''