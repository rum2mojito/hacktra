import unittest

from gameData.downloadTroopData import downloadTroopData

class TestDAO(unittest.TestCase):
  def test_connection(self):
    url = "https://t4.answers.travian.com/index.php?view=answers&action=answer&cid=203"
    re = downloadTroopData(url)
    re.getContent(url)
    self.assertEquals(re.getContent(url), True)

if __name__ == '__main__':
  unittest.main()