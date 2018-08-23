# from gameData.downloadTroopData import downloadTroopData
from metastore.dao.DAO import DAO
# from dist.troop import troop

class troopDataDAO(DAO):
  def insertUpdateData(self, troop, level):
    query = 'INSERT INTO ' + troop.name
    query += ' VALUES '
    query += '(NULL, ' + troop.cid + ', ' \
             + troop.level[level] + ', ' \
             + troop.needLumber[level] + ', ' \
             + troop.needClay[level] + ', ' \
             + troop.needIron[level] + ', ' \
             + troop.needCrop[level] + ', ' \
             + troop.trainTimeL1[level] + ', '\
             + troop.trainTimeL2[level] + ')'
    return self.query(query)

  def insertTrainData(self, troop):
    query = 'INSERT INTO ' + 'troop'
    query += ' VALUES '
    query += '(NULL, ' + troop.cid + ', ' \
             + troop.trainLumber + ', ' \
             + troop.trainClay + ', ' \
             + troop.trainIron + ', ' \
             + troop.trainCrop + ', ' \
             + troop.velocity + ', ' \
             + troop.carry + ', ' \
             + troop.attack + ', ' \
             + troop.infantry + ', ' \
             + troop.cavalry + ', ' \
             + troop.resLumber + ', ' \
             + troop.resClay + ', ' \
             + troop.resIron + ', ' \
             + troop.resCrop + ', ' \
             + troop.resTime + ')'
    a = query
    return self.query(query)

  def createTroopTable(self):
    try:
      self.c.execute("""CREATE TABLE troop 
                          (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Cid text NOT NULL,
                          Lumber text NOT NULL,
                          Clay text NOT NULL,
                          Iron text NOT NULL,
                          Crop text NOT NULL,
                          Velocity text NOT NULL,
                          Carry text NOT NULL,
                          Attack text NOT NULL,
                          Infantry text NOT NULL,
                          Cavalry text NOT NULL,
                          ResLumber text NOT NULL,
                          ResClay text NOT NULL,
                          ResIron text NOT NULL,
                          ResCrop text NOT NULL,
                          ResTime text NOT NULL
                          );""")
      self.logger.info('CREATED TABLE troop')
    except Exception as err:
      self.logger.warn(err)

  def createTroopUpdateTable(self, troop):
    try:
      a = troop.name
      self.c.execute("""CREATE TABLE """ + troop.name + """
                          (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Cid text NOT NULL,
                          Level text NOT NULL,
                          Lumber text NOT NULL,
                          Clay text NOT NULL,
                          Iron text NOT NULL,
                          Crop text NOT NULL,
                          Time text NOT NULL,
                          Time2 text NOT NULL
                          );""")
      self.logger.info('CREATED TABLE ' + troop.name)
    except Exception as err:
      self.logger.warn(err)

  def __init__(self):
    super(troopDataDAO, self).__init__('troopData')

  def __del__(self):
    super(troopDataDAO, self).__del__()
