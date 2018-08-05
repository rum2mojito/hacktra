from gameData.downloadTroopData import downloadTroopData
from metastore.dao.DAO import DAO

class troopDataDAO(DAO):
  def createTable(self, tableName):
    sql = """"""

  def __init__(self):
    super(troopDataDAO, self).__init__('troopData')

  def __del__(self):
    super(troopDataDAO, self).__del__()
