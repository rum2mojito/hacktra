import sqlite3
import logging
import xlwt


class DAO:
  def query(self, query):
    self.logger.debug(query)
    try:
      self.c.execute(query)
      return True
    except Exception as err:
      self.logger.error(str(err))
      return False

  def connectDB(self):
    """ connect to database
    :return: True for success
    """
    try:
      self.conn = sqlite3.connect(self.DBName + '.db')
      self.c = self.conn.cursor()
      self.logger.debug('CONNECT TO {}'.format(self.DBName + '.db'))
      return True
    except Exception as err:
      self.logger.error(str(err))
      return False

  def __init__(self, DB):
    """ initial class DAO with logger and connect to database
    :param DBName: database name
    """
    self.logger = logging.getLogger('DAO.py')
    self.DBName = DB
    self.connectDB()

  def __del__(self):
    """ disconnect from database
    :return: None
    """
    try:
      self.conn.commit()
      self.conn.close()
      # self.logger.info('Disconnect from ' + self.DBName + '.db')
    except Exception as err:
      self.logger.error(str(err))
